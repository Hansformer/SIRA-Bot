import logging
import os
import re
import warnings
from pathlib import Path

import hikari
from hikari import Intents
from hikari.snowflakes import Snowflake
import tanjun

import config

if os.name != 'nt':
    import uvloop
    uvloop.install()

my_intents = (
    Intents.ALL_UNPRIVILEGED |
    Intents.GUILD_MEMBERS
)

logger = logging.getLogger('sirabot')
logger.setLevel(logging.INFO)

if config.DEBUG:
    logging.getLogger('asyncio').setLevel(logging.DEBUG)
    warnings.simplefilter('default')
    logger.setLevel(logging.DEBUG)

logger.info('Initializing SIRA Bot...')
bot = hikari.GatewayBot(config.TOKEN, intents=my_intents)
client = tanjun.Client.from_gateway_bot(bot, declare_global_commands=Snowflake(config.GUILD_ID))
client.load_modules(*Path('modules').glob('*.py'))


@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    guild = await event.app.rest.fetch_guild(config.GUILD_ID)
    await guild.get_channel(config.BOT_CHANNEL).send('SIRA Bot signing off. <:o7:365926799613624330>')


@bot.listen()
async def on_stopped(_: hikari.StoppedEvent) -> None:
    logger.info('SIRA Bot disengaged.')


@bot.listen()
async def on_shard_ready(event: hikari.ShardReadyEvent) -> None:
    logger.info('Connected to Discord')
    logger.info('Username: %s', event.my_user.username)
    logger.info('ID: %s', event.my_user.id)
    guild = await event.app.rest.fetch_guild(config.GUILD_ID)
    await guild.get_channel(config.BOT_CHANNEL).send('SIRA Bot reporting for duty. '
                                                     '<:o7:365926799613624330>')


@bot.listen()
async def on_member_create(event: hikari.MemberCreateEvent) -> None:
    logger.info('User joined - %s', event.user.username)
    chan = event.get_guild().get_channel(config.WELCOME_CHANNEL)
    await chan.send(f'Welcome {event.user.mention}.'
                    ' <:vision_intensifies:332951986645499904>\n'
                    'If you have any issues, please tag an '
                    '<@&200367057378869248>.')
    await chan.send('Be sure to join the /edg/ group (SIRA) - '
                    '<:space_ireland:309204831548211201> - '
                    '<https://inara.cz/wing/1470>')


@bot.listen()
async def on_member_delete(event: hikari.MemberDeleteEvent) -> None:
    logger.info('User left - %s', event.user.username)
    await event.get_guild().get_channel(config.ADMIN_CHANNEL).send(f'{event.user.mention} ({event.user.username}) '
                                                                   'has quit. <:umaru_cry:319973822012981248>')


@bot.listen()
async def process_reactions(event: hikari.GuildMessageCreateEvent) -> None:
    logger.debug('New message in %s - %s: %s', event.get_channel(), event.author, event.content)

    if event.is_bot or not event.content:
        return

    regex_reactions =\
        {r'\bs\s?p\s?a\s?c\s?e(?:\s?|_)i\s?r\s?e\s?l\s?a\s?n\s?d\b':
         ':space_ireland:309204831548211201',
         r'\*|_bombs u\*|_': '\U0001F4A3'}

    reactions = {f'{await event.shard.get_user_id()}>': ':anime_smug:319973746825756683'}

    for regex, reaction in regex_reactions.items():
        if re.search(regex, event.content, re.I):
            await event.message.add_reaction(reaction)

    for trigger, reaction in reactions.items():
        if trigger in event.content:
            await event.message.add_reaction(reaction)
            if reaction == '\U0001F4A3':
                await event.message.respond('Space Ireland will be free! '
                                            '<:space_ireland:309204831548211201>')

#   # soon
#   if re.search(r'\bs\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s\b',
#               message.content, re.I)\
#   or re.search(
#       r'\ba\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?(?:e|i\s?c)\s?s?\b',
#       message.content, re.I):
#       await self.send_message(
#           chan,
#           'SOON:tm: <:smiling_man:332954734975647754>')

# member update routine
# async def on_member_update(self, before, after):
#     server = self.get_server('195647497505472512')
#
#     # auto tag the heathens
#     if 'EVE Online' in f'{after.game}':
#         role = discord.utils.get(server.roles, id='207087337958539274')
#         if role not in after.roles:
#             await self.add_roles(after, role)
#             logger.info(f'{after.name} auto-tagged as EVE heathen.')

bot.run()
