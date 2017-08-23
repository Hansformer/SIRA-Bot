# required libs
import re
import os
from functools import partial

import discord
from pluginbase import PluginBase

# discord api config
import config
from sirabot.utils import get_time


class SIRABot(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        here = os.path.abspath(os.path.dirname(__file__))
        get_path = partial(os.path.join, here)
        plugin_base = PluginBase(package='sirabot.plugins')
        self.plugin_source = plugin_base.make_plugin_source(
            searchpath=[get_path('./sirabot/plugins')])
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    async def process_reactions(self, message):
        regex_reactions =\
            {r'\bs\s?p\s?a\s?c\s?e(?:\s?|_)i\s?r\s?e\s?l\s?a\s?n\s?d\b':
             ':space_ireland:309204831548211201',
             r'\bw\s?e\s?w(?:\slad)?\b': ':wew:319973823040716804',
             r'v\s?i\s?s\s?i\s?o\s?n':
             ':vision_intensifies:332951986645499904'}
        reactions = {'o7': ':o7:308408906344824852'}

        for regex, reaction in regex_reactions.items():
            if re.search(regex, message.content, re.I):
                await self.add_reaction(message, reaction)
                if reaction == ':wew:319973823040716804':
                    await self.send_message(message.channel, 'wew')

        for trigger, reaction in reactions.items():
            if trigger in message.content:
                await self.add_reaction(message, reaction)

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
        for plugin_name in self.plugin_source.list_plugins():
            plugin = self.plugin_source.load_plugin(plugin_name)
            await plugin.setup(self)

        tstamp = get_time()

        # print some console info
        print(f"[{tstamp}] Initializing SIRA Bot...")
        print('-----INFO-----')
        print(self.user.name)
        print(self.user.id)
        print('--------------')
        print(f"[{tstamp}] It lives.")

        # send a message
        chan = self.get_channel('348971376750886912')
        await self.send_message(
            chan,
            'SIRA Bot reporting for duty. <:o7:308408906344824852>')

    # member join routine
    async def on_member_join(self, member):
        tstamp = get_time()
        print(f"[{tstamp}] User joined - {member.name}")
        chan = self.get_channel('195647497505472512')
        await self.send_message(
            chan,
            f"Welcome <@!{member.id}>."
            " <:vision_intensifies:332951986645499904> "
            "If you have any issues, please tag an <@&200367057378869248>.")
        await self.send_message(
            chan,
            "Join the /edg/ player group, SIRA - https://inara.cz/wing/1470")

    # member quit routine
    @staticmethod
    async def on_member_remove(member):
        tstamp = get_time()
        print(f"[{tstamp}] User left - {member.name}")

    # on message routine
    async def on_message(self, message):
        tstamp = get_time()
        chan = message.channel

        # reactions (no self reactions)
        if message.author.id != self.user.id:
            await self.process_reactions(message)

        # soon
        if re.search(r'\bs\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s\b',
                     message.content, re.I)\
            or re.search(r'\ba\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?(?:e|i\s?c)\b',
                         message.content, re.I):
            await self.send_message(
                chan,
                'SOON:tm: <:smiling_man:332954734975647754>')

        # react to being mentioned
        if f'<@!{self.user.id}>' in message.content:
            await self.add_reaction(
                message,
                ':anime_smug:319973746825756683')
            await self.send_message(
                chan,
                'You noticed me, senpai.')

        # sira-bot is patriotic
        if '*bombs u*' in message.content:
            await self.add_reaction(
                message,
                "\U0001F4A3")
            await self.send_message(
                chan,
                'Space Ireland will be free!'
                ' <:space_ireland:309204831548211201>')

        if message.content.startswith('!'):
            await self.process_commands(message)

        # if debug is enabled print a message log in the console
        if config.debug:
            print(f"[{tstamp}] New message in {message.channel} -"
                  f" {message.author}: {message.content}")

# running the bot
bot = SIRABot()
bot.run(config.token)
