# required libs
import discord
import asyncio
import time
import datetime
import re

# discord api config
'''
Create a local configuration file (config.py) with the following:
username = "String value"                                                   
password = "String value"
token = "String value"
debug = False
'''
from config import *

# var defs
client = discord.Client()
chan = None

# login routine
@client.event
@asyncio.coroutine
def on_ready():
    t = time.time()
    ts = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    # print some console info
    print("[%s] Initializing SIRA Bot..." % ts)
    print('-----INFO-----')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    print("[%s] It lives." % (ts))
    # send a message
    chan = client.get_channel('348971376750886912')
    yield from client.send_message (chan,
                                    'SIRA Bot reporting for duty. <:o7:308408906344824852>')

# member join routine
@client.event
@asyncio.coroutine
def on_member_join(member):
    t = time.time()
    ts = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] User joined - %s" % (ts, member.name))
    chan = client.get_channel('195647497505472512')
    m = member.id
    yield from client.send_message (chan,
                                    "Welcome <@!%s>. <:vision_intensifies:332951986645499904> If you have any issues, please tag an <@&200367057378869248>." % m)
    yield from client.send_message (chan,
                                    "Join the /edg/ player group, SIRA - https://inara.cz/wing/1470")
# member quit routine
@client.event
@asyncio.coroutine
def on_member_remove(member):
    t = time.time()
    ts = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    print("[%s] User left - %s" % (ts, member.name))


# on message routine
@client.event
@asyncio.coroutine
def on_message(message):
    t = time.time()
    ts = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    chan = message.channel
    x = message.content.lower()
    y = x.replace(" ", "")

    if message.author.id != '319826689729232897':
        # space ireland reactions
        if (message.content.find('<:space_ireland:309204831548211201>') != -1 or 
            re.search(r'(s\s?p\s?a\s?c\s?e\s*i\s?r\s?e\s?l\s?a\s?n\s?d)+\b', x)):
            yield from client.add_reaction (message, 
                                            ':space_ireland:309204831548211201')

        # o7 reactions
        if (message.content.find('<:o7:308408906344824852>') != -1 or 
            message.content.find('o7') != -1):
            yield from client.add_reaction (message, 
                                            ':o7:308408906344824852')
        # wew
        if re.search(r'(w\s?e\s?w(\slad)?)+\b', x):
            yield from client.add_reaction (message,
                                            ':wew:319973823040716804')
            yield from client.send_message (chan,
                                            'wew')

    # react to being mentioned
    if message.content.find('<@!319826689729232897>') != -1:
        yield from client.add_reaction (message,
                                        ':anime_smug:319973746825756683')
        yield from client.send_message (chan,
                                        'You noticed me, senpai.')

    # sira-bot is patriotic
    if message.content.find('*bombs u*') != -1:
        yield from client.add_reaction (message,
                                        u"\U0001F4A3")
        yield from client.send_message (chan,
                                        'Space Ireland will be free! <:space_ireland:309204831548211201>')

    # space legs
    if (re.search(r'(s\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s)+\b', x) or
        re.search(r'(a\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?i\s?c)+', x)):
        yield from client.send_message (chan,
                                        'SOON:tm: <:smiling_man:332954734975647754>')

    # admin commands
    if (message.author.id == '189890760873738240' or
        message.author.id == '156405315976429568'):
    
        # kill/close
        if (message.content.startswith('!botkill') or
            message.content.startswith('!kill') or
            message.content.startswith('!close') or
            message.content.startswith('!end')):
            # send a message and kill the script
            print("[%s] SIRA Bot disengaged." % ts)
            chan = client.get_channel('348971376750886912')
            yield from client.send_message (chan,
                                            'SIRA Bot signing off. <:o7:308408906344824852>')
            yield from client.close()

        # idle
        if message.content.startswith('!rest'):
            yield from client.change_presence(game=discord.Game(name='recharging'), status=discord.Status('idle'), afk=True)

        #vision
        if message.content.startswith('!vision'):
            yield from client.change_presence(game=discord.Game(name='v i s i o n'), status=discord.Status('online'), afk=False)

    # if debug is enabled print a message log in the console
    if debug:
        print("[%s] New message in %s - %s: %s" % (ts, message.channel, message.author, message.content))

# running the bot
client.login(username, password)
client.run(token)