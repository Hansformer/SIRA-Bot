# required libs
import asyncio
import re
import os
import sys
import logging
import warnings
import signal
from functools import partial

import discord
from pluginbase import PluginBase
import aiofiles

# discord api config
import config

# logging
if config.debug:
    logging.getLogger('asyncio').setLevel(logging.DEBUG)
    warnings.simplefilter('default')

logger = logging.getLogger('sirabot')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = logging.FileHandler(config.logfile)

if config.debug:
    ch.setLevel(logging.DEBUG)
    fh.setLevel(logging.DEBUG)
else:
    ch.setLevel(logging.WARNING)
    fh.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:'
                              ' %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


# exception logging
def log_exception(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception",
                 exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = log_exception


# bot class and main functions
class SIRABot(discord.Client):

    # initialization
    def __init__(self, **options):
        logger.info('Initializing SIRA Bot...')
        super().__init__(**options)
        if config.debug:
            self.loop.set_debug(True)
        for signame in ('SIGINT', 'SIGTERM'):
            self.loop.add_signal_handler(getattr(signal, signame),
                                         lambda: asyncio.ensure_future(
                                             self.kill(signame)))
        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)
        plugin_base = PluginBase(package='sirabot.plugins')
        self.plugin_source = plugin_base.make_plugin_source(
            searchpath=[get_path('./sirabot/plugins')])
        self.commands = {}
        self.log = logger

    # kill routine
    async def kill(self, signame='SIGINT'):
        logger.debug(f'Received {signame}')
        chan = self.get_channel('348971376750886912')
        await self.send_message(
            chan,
            'SIRA Bot signing off. <:o7:365926799613624330>')
        await self.logout()
        logger.info('SIRA Bot disengaged.')

    # registering commands
    def register_command(self, name, command):
        self.commands[name] = command

    # processing reactions
    async def process_reactions(self, message):
        chan = message.channel

        # regex definitions
        regex_reactions =\
            {r'\bs\s?p\s?a\s?c\s?e(?:\s?|_)i\s?r\s?e\s?l\s?a\s?n\s?d\b':
             ':space_ireland:309204831548211201'}

        # reaction definitions
        reactions = {f'{self.user.id}>': ':anime_smug:319973746825756683',
                     '*bombs u*': "\U0001F4A3"}

        # regex triggers
        for regex, reaction in regex_reactions.items():
            if re.search(regex, message.content, re.I):
                await self.add_reaction(message, reaction)

        # reaction triggers
        for trigger, reaction in reactions.items():
            if trigger in message.content:
                await self.add_reaction(message, reaction)
                if reaction == "\U0001F4A3":
                    await self.send_message(
                        chan, 'Space Ireland will be free! '
                        '<:space_ireland:309204831548211201>')

    # processing messages
    async def process_message(self, message):
        chan = message.channel

    #   # soon
    #   if re.search(r'\bs\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s\b',
    #               message.content, re.I)\
    #   or re.search(
    #       r'\ba\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?(?:e|i\s?c)\s?s?\b',
    #       message.content, re.I):
    #       await self.send_message(
    #           chan,
    #           'SOON:tm: <:smiling_man:332954734975647754>')

    # processing commands
    async def process_commands(self, message):
        try:
            command, parameter = message.content[1:].split(' ', 1)
        except ValueError:
            command = message.content[1:]
            parameter = None

        if command in self.commands:
            await self.commands[command](self, message, parameter)

    # login routine
    async def on_ready(self):
        logger.info("Connected to Discord")
        logger.info(f'Username: {self.user.name}')
        logger.info(f'ID: {self.user.id}')
        async with aiofiles.open('images/siraicon.png', mode='rb') as f:
            contents = await f.read()
        await self.edit_profile(avatar=contents)
        logger.debug('Loading plugins')
        for plugin_name in self.plugin_source.list_plugins():
            plugin = self.plugin_source.load_plugin(plugin_name)
            await plugin.setup(self)
        logger.debug('Plugins loaded')

        # send a message
        chan = self.get_channel('348971376750886912')
        await self.send_message(
            chan,
            'SIRA Bot reporting for duty. <:o7:365926799613624330>')

    # member join routine
    async def on_member_join(self, member):
        logger.info(f"User joined - {member.name}")
        chan = self.get_channel('195647497505472512')
        await self.send_message(
            chan,
            f"Welcome {member.mention}."
            " <:vision_intensifies:332951986645499904>\n"
            "If you have any issues, please tag an <@&200367057378869248>.")
        await self.send_message(
            chan,
            f"Be sure to join the /edg/ group (SIRA) - "
            "<:space_ireland:309204831548211201> - "
            "<https://inara.cz/wing/1470>")

    # member quit routine
    async def on_member_remove(self, member):
        logger.info(f"User left - {member.name}")
        chan = self.get_channel('200383687232192513')
        await self.send_message(
            chan,
            f"{member.mention} ({member.name}) has quit. "
            "<:umaru_cry:319973822012981248>")

    # on message routine
    async def on_message(self, message):
        # react to messages (no self reactions)
        if message.author.id != self.user.id:

            # trigger ! commands
            if message.content.startswith('!'):
                await self.process_commands(message)

            else:
                await self.process_reactions(message)
    #           await self.process_message(message)

        # if debug is enabled print a message log in the console
        logger.debug(f"New message in {message.channel} -"
                     f" {message.author}: {message.content}")

    # member update routine
    # async def on_member_update(self, before, after):
    #     server = self.get_server('195647497505472512')
    #
    #     # auto tag the heathens
    #     if 'EVE Online' in f'{after.game}':
    #         role = discord.utils.get(server.roles, id='207087337958539274')
    #         if role not in after.roles:
    #             await self.add_roles(after, role)
    #             logger.info(f"{after.name} auto-tagged as EVE heathen.")

    async def on_error(self, event_method, *args, **kwargs):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        log_exception(exc_type, exc_value, exc_traceback)


# running the bot
if config.token != 'token':
    bot = SIRABot()
    bot.run(config.token)
else:
    logger.error('Token not set')
