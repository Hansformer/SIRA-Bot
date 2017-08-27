import discord
from sirabot.utils import is_admin


# kill command
@is_admin
async def kill(client, message, parameter):
    await client.kill()


# idle status
@is_admin
async def idle(client, message, parameter):
    await client.change_presence(game=discord.Game(name='with live wires'),
                                 status=discord.Status('idle'),
                                 afk=True)
    await client.send_message(message.channel, '...')


# vision status
@is_admin
async def vision(client, message, parameter):
    await client.change_presence(game=discord.Game(name='the v i s i o n'),
                                 status=discord.Status('online'),
                                 afk=False)
    await client.send_message(message.channel, 'I have been visioned.')


# trigger definitions
async def setup(client):
    for alias in ['botkill', 'kill', 'close', 'end', 'kys',
                  'ded', 'rip', 'makeded', 'fuckoff']:
        client.register_command(alias, kill)
    for alias in ['rest', 'idle', 'recharge', 'status2']:
        client.register_command(alias, idle)
    for alias in ['vision', 'status1']:
        client.register_command(alias, vision)
