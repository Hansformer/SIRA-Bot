# required libs
import re
import aiohttp
import pendulum

import discord
from discord.ext import commands

# discord api config
import config

# var defs
description = 'Discord bot for SIRA'
bot = commands.Bot(command_prefix='!', description=description)


# timestamp formatting for console/terminal
def get_time():
    zone = pendulum.timezone(config.tzone)
    stamp = pendulum.now(zone).strftime(config.tformat)
    return stamp


def is_admin(fn):
    async def ret_fn(ctx):
        if ctx.message.author.id in config.admins:
            return fn(ctx)
        else:
            raise Exception('Unauthorized')
    return ret_fn


async def process_reactions(message):
    regex_reactions = {r'(s\s?p\s?a\s?c\s?e\s*i\s?r\s?e\s?l\s?a\s?n\s?d)+\b':
                       ':space_ireland:309204831548211201',
                       r'(w\s?e\s?w(\slad)?)+\b': ':wew:319973823040716804',
                       r'(v\s?i\s?s\s?i\s?o\s?n)+':
                           ':vision_intensifies:332951986645499904'}
    reactions = {'<:o7:308408906344824852>': ':o7:308408906344824852',
                 '<:space_ireland:309204831548211201>':
                     ':space_ireland:309204831548211201'}

    for regex, reaction in regex_reactions.items():
        if re.search(regex, message.content, re.I):
            await bot.add_reaction(message, reaction)
            if reaction == ':wew:319973823040716804':
                await bot.send_message(message.channel, 'wew')

    for trigger, reaction in reactions.items():
        if trigger in message.content:
            await bot.add_reaction(message, reaction)


# get server status from EDSM API
@bot.event
async def check_server():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://www.edsm.net/api-status-v1/elite-server'
                ) as resp:
            api = await resp.json()
            return api['type'], api['message']


# login routine
@bot.event
async def on_ready():
    tstamp = get_time()

    # print some console info
    print("[%s] Initializing SIRA Bot..." % tstamp)
    print('-----INFO-----')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')
    print("[%s] It lives." % tstamp)

    # send a message
    chan = bot.get_channel('348971376750886912')
    await bot.send_message(
        chan,
        'SIRA Bot reporting for duty. <:o7:308408906344824852>')


# member join routine
@bot.event
async def on_member_join(member):
    tstamp = get_time()
    print("[%s] User joined - %s" % (tstamp, member.name))
    chan = bot.get_channel('195647497505472512')
    await bot.send_message(
        chan,
        "Welcome <@!%s>. <:vision_intensifies:332951986645499904> "
        "If you have any issues, please tag an <@&200367057378869248>."
        % member.id)
    await bot.send_message(
        chan,
        "Join the /edg/ player group, SIRA - https://inara.cz/wing/1470")


# member quit routine
@bot.event
async def on_member_remove(member):
    tstamp = get_time()
    print("[%s] User left - %s" % (tstamp, member.name))


# on message routine
@bot.event
async def on_message(message):
    tstamp = get_time()
    chan = message.channel

    # reactions (no self reactions)
    if message.author.id != bot.user.id:
        await process_reactions(message)

    # soon
    if re.search(r'(s\s?p\s?a\s?c\s?e\s*l\s?e\s?g\s?s)+\b',
                 message.content, re.I)\
            or re.search(r'(a\s?t\s?m\s?o\s?s\s?p\s?h\s?e\s?r\s?i\s?c)+',
                         message.content, re.I):
        await bot.send_message(
            chan,
            'SOON:tm: <:smiling_man:332954734975647754>')

    # react to being mentioned
    if '<@!{}>'.format(bot.user.id) in message.content:
        await bot.add_reaction(
            message,
            ':anime_smug:319973746825756683')
        await bot.send_message(
            chan,
            'You noticed me, senpai.')

    # sira-bot is patriotic
    if '*bombs u*' in message.content:
        await bot.add_reaction(
            message,
            "\U0001F4A3")
        await bot.send_message(
            chan,
            'Space Ireland will be free! <:space_ireland:309204831548211201>')

    await bot.process_commands(message)

    # if debug is enabled print a message log in the console
    if config.debug:
        print("[%s] New message in %s - %s: %s" % (
            tstamp,
            message.channel,
            message.author,
            message.content))


@bot.command(aliases=['status'])
async def server():
    sstatus, smsg = await check_server()
    if sstatus == 'success':
        await bot.say('FDev says "%s". :ok_hand:' % smsg)
    elif sstatus == 'warning':
        await bot.say(':warning: FDev says "%s".' % smsg)
    elif sstatus == 'danger':
        await bot.send_message(
            ':fire: "%s". Sandro tripped over the server cords again.' % smsg)


@bot.command(pass_context=True)
async def flag(ctx):
    await bot.send_file(ctx.message.channel, "flag_of_space_ireland.png")


@is_admin
@bot.command(aliases=['botkill', 'close', 'end', 'ded',
                      'rip', 'makeded', 'fuckoff'], pass_context=True)
async def kill(ctx):
    # send a message and kill the script
    print("[%s] SIRA Bot disengaged." % get_time())
    chan = bot.get_channel('348971376750886912')
    await bot.send_message(chan,
                           'SIRA Bot signing off. <:o7:308408906344824852>')
    await bot.close()


@is_admin
@bot.command(aliases=['rest', 'recharge'], pass_context=True)
async def idle(ctx):
    await bot.change_presence(game=discord.Game(name='recharging'),
                              status=discord.Status('idle'), afk=True)


@is_admin
@bot.command(pass_context=True)
async def vision(ctx):
    await bot.change_presence(game=discord.Game(name='v i s i o n'),
                              status=discord.Status('online'), afk=False)

# running the bot
bot.run(config.token)
