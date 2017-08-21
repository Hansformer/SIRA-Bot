# required libs
import discord
import asyncio
import re
import pendulum
import aiohttp
import json

# discord api config
'''
Create a local configuration file (config.py) with the following:
username = "String value"
password = "String value"
token = "String value"
debug = Boolean
tzone = "String value"
tformat = "String value"
'''
from config import *

# var defs
client = discord.Client()
chan = None
sstatus = None
smsg = None
tstamp = None


def get_time():
    zone = pendulum.timezone(tzone)
    stamp = pendulum.now(zone).strftime(tformat)
    return stamp


@client.event
async def check_server():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.edsm.net/api-status-v1/elite-server') as resp:
            api = await resp.json()
            return api['type'], api['message']


# login routine
@client.event
@asyncio.coroutine
def on_ready():
    tstamp = get_time()
    # print some console info
    print("[%s] Initializing SIRA Bot..." % tstamp)
    print('-----INFO-----')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    print("[%s] It lives." % (tstamp))
    # send a message
    chan = client.get_channel('348971376750886912')
    yield from client.send_message(
        chan,
        'SIRA Bot reporting for duty. <:o7:308408906344824852>')


# member join routine
@client.event
@asyncio.coroutine
def on_member_join(member):
    tstamp = get_time()
    print("[%s] User joined - %s" % (tstamp, member.name))
    chan = client.get_channel('195647497505472512')
    m = member.id
    yield from client.send_message(
        chan,
        "Welcome <@!%s>. <:vision_intensifies:332951986645499904> "
        "If you have any issues, please tag an <@&200367057378869248>." % m)
    yield from client.send_message(
        chan,
        "Join the /edg/ player group, SIRA - https://inara.cz/wing/1470")


# member quit routine
@client.event
@asyncio.coroutine
def on_member_remove(member):
    tstamp = get_time()
    print("[%s] User left - %s" % (tstamp, member.name))


# on message routine
@client.event
@asyncio.coroutine
def on_message(message):
    tstamp = get_time()
    chan = message.channel
    x = message.content.lower()

    if message.content.startswith('!'):
        try:
            command, parameter = message.content[1:].split(' ', 1)
        except ValueError:
            command = message.content[1:]
            parameter = None

        # admin commands
        if(message.author.id == '189890760873738240' or
           message.author.id == '156405315976429568'
           ):
            
            if command in ['botkill', 'kill', 'close', 'end', 'ded', 'rip',
                'makeded', 'fuckoff']:

                # send a message and kill the script
                print("[%s] SIRA Bot disengaged." % tstamp)
                chan = client.get_channel('348971376750886912')
                yield from client.send_message(
                    chan,
                    'SIRA Bot signing off. <:o7:308408906344824852>')
                yield from client.close()

            # idle
            if command in ['rest', 'idle', 'recharge']:
                yield from client.change_presence(
                    game=discord.Game(name='recharging'),
                    status=discord.Status('idle'),
                    afk=True)

            # vision
            if command in ['vision']:
                yield from client.change_presence(
                    game=discord.Game(name='v i s i o n'),
                    status=discord.Status('online'),
                    afk=False)

    # no self reactions
    if message.author.id != '319826689729232897':
        # space ireland reactions
        if(message.content.find('<:space_ireland:309204831548211201>') != -1 or
           re.search(r'(s\s?p\s?a\s?c\s?e\s*i\s?r\s?e\s?l\s?a\s?n\s?d)+\b',
                     x)
           ):
            yield from client.add_reaction(
                message,
                ':space_ireland:309204831548211201')

        # o7 reactions
        if(message.content.find('<:o7:308408906344824852>') != -1 or
           message.content.find('o7') != -1
           ):
            yield from client.add_reaction(message,
                                           ':o7:308408906344824852')
        # wew
        if re.search(r'(w\s?e\s?w(\slad)?)+\b', x):
            yield from client.add_reaction(message,
                                           ':wew:319973823040716804')
            yield from client.send_message(chan,
                                           'wew')

        # v i s i o n
        if re.search(r'(v\s?i\s?s\s?i\s?o\s?n)+', x):
            yield from client.add_reaction(
                message,
                ':vision_intensifies:332951986645499904')

    # react to being mentioned
    if message.content.find('<@!319826689729232897>') != -1:
        yield from client.add_reaction(message,
                                       ':anime_smug:319973746825756683')
        yield from client.send_message(chan,
                                       'You noticed me, senpai.')

    # sira-bot is patriotic
    if message.content.find('*bombs u*') != -1:
        yield from client.add_reaction(message,
                                       u"\U0001F4A3")
        yield from client.send_message(
            chan,
            'Space Ireland will be free! <:space_ireland:309204831548211201>')

    # flag
    if message.content.startswith('!flag'):
        yield from client.send_file(
            chan,
            "C:/SIRA/SIRA-Bot-Rebirth/flag_of_space_ireland.png")

    # space legs
    if(re.search(r'(s\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s)+\b', x) or
       re.search(r'(a\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?i\s?c)+', x)
       ):
        yield from client.send_message(
            chan,
            'SOON:tm: <:smiling_man:332954734975647754>')

    # server status
    if message.content.startswith('!server'):
        sstatus, smsg = yield from check_server()
        if sstatus == 'success':
            yield from client.send_message(
                chan,
                'FDev says "%s". :ok_hand:' % smsg)
        elif sstatus == 'warning':
            yield from client.send_message(
                chan,
                ':warning: FDev says "%s".' % smsg)
        elif sstatus == 'danger':
            yield from client.send_message(
                chan,
                ':fire: "%s". Sandro tripped over the server cords again.' 
                % smsg)

    # if debug is enabled print a message log in the console
    if debug:
        print("[%s] New message in %s - %s: %s" % (
            tstamp,
            message.channel,
            message.author,
            message.content))


# running the bot
client.login(username, password)
client.run(token)
