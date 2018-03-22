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
    await client.change_presence(game=discord.Game(name='V I S I O N'),
                                 status=discord.Status('online'),
                                 afk=False)
    await client.send_message(message.channel,
                              'I have been V I S I O N\'d.'
                              ' <:vision_intensifies:332951986645499904>')


# trigger definitions
async def setup(client):
    for alias in ['kill', 'close', 'end', 'kys', 'ded', 'rip', 'makeded']:
        client.register_command(alias, kill)
    client.register_command('idle', idle)
    client.register_command('vision', vision)
