import discord
import aiofiles

from sirabot.utils import is_admin


# kill command
@is_admin
async def kill(client, message, parameter):
    await client.kill()


# idle status
@is_admin
async def idle(client, message, parameter):
    await client.change_presence(status=discord.Status.idle,
                                 activity=discord.Game(name='with live wires'),
                                 afk=True)

    await message.channel.send('...')


# vision status
@is_admin
async def vision(client, message, parameter):
    await client.change_presence(activity=discord.Game(name='V I S I O N'),
                                 afk=False)
    await message.channel.send('I have been V I S I O N\'d.'
                               ' <:vision_intensifies:332951986645499904>')


@is_admin
async def avatar(client, message, parameter):
    async with aiofiles.open('images/siraicon.png', mode='rb') as file:
        contents = await file.read()
    await client.edit_profile(avatar=contents)


# trigger definitions
async def setup(client):
    for alias in ['kill', 'close', 'end', 'kys', 'ded', 'rip', 'makeded']:
        client.register_command(alias, kill)
    client.register_command('idle', idle)
    client.register_command('vision', vision)
