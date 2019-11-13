from discord import File


# flag command
async def flag_showimg(client, message, parameter):
    await message.channel.send(file=File("../../images/flag_of_space_ireland.png"))


# new battleflag command
async def battle_flag_showimg(client, message, parameter):
    await message.channel.send(file=File("../../images/battleflag.png"))


# logo command
async def logo_showimg(client, message, parameter):
    await message.channel.send(file=File("../../images/sira_logo.png"))


# Bhadaba! meme command
async def bhadaba_showimg(client, message, parameter):
    await message.channel.send(file=File("../../images/Bhadaba.jpg"))


# asp meme command
async def asp_showimg(client, message, parameter):
    await message.channel.send(file=File("../../images/ASP.png"))


# trigger definitions
async def setup(client):

    # flags
    client.register_command('flag', flag_showimg)
    for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battle_flag_showimg)

    # logo
    client.register_command('logo', logo_showimg)

    # other memes
    client.register_command('bhadaba', bhadaba_showimg)
    client.register_command('ASP', asp_showimg)
