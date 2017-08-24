import discord
from sirabot.utils import is_admin


@is_admin
async def kill(client, message, parameter):
    await client.kill()


@is_admin
async def idle(client, message, parameter):
    await client.change_presence(game=discord.Game(name='recharging'),
                                 status=discord.Status('idle'),
                                 afk=True)


@is_admin
async def vision(client, message, parameter):
    await client.change_presence(game=discord.Game(name='v i s i o n'),
                                 status=discord.Status('online'),
                                 afk=False)


async def setup(client):
    for alias in ['botkill', 'kill', 'close', 'end', 'kys',
                  'ded', 'rip', 'makeded', 'fuckoff']:
        client.register_command(alias, kill)
    for alias in ['rest', 'idle', 'recharge', 'status2']:
        client.register_command(alias, idle)
    for alias in ['vision', 'status1']:
        client.register_command(alias, vision)
