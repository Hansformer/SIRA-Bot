from discord import File


# flag command
async def flag_showimg(client, message, parameter):
    await message.channel.send(file=File("images/flag_of_space_ireland.png"))


# new battleflag command
async def battle_flag_showimg(client, message, parameter):
    await message.channel.send(file=File("images/battleflag.png"))


# logo command
async def logo_showimg(client, message, parameter):
    await message.channel.send(file=File("images/sira_logo.png"))


# Bhadaba! meme command
async def bhadaba_showimg(client, message, parameter):
    await message.channel.send(file=File("images/Bhadaba.jpg"))


# asp meme command
async def asp_showimg(client, message, parameter):
    await message.channel.send(file=File("images/ASP.png"))


# landmine meme command
async def landmine_showimg(client, message, parameter):
    await message.channel.send(file=File("images/landmines.jpg"))


# skimmer meme command
async def skimmer_showimg(client, message, parameter):
    await message.channel.send(file=File("images/what_is_a_skimmer.png"))


# stay safe meme command
async def safe_showimg(client, message, parameter):
    await message.channel.send(file=File("images/stay_safe_everyone.jpg"))


# conquest meme command
async def conquest_showimg(client, message, parameter):
    await message.channel.send(file=File("images/achievement_meme.png"))


# aisling meme command
async def aisling_showimg(client, message, parameter):
    await message.channel.send(file=File("images/aisling.jpg"))


# brabo biowaste meme command
async def brabowaste_showimg(client, message, parameter):
    await message.channel.send(file=File("images/brabowaste.png"))


# parnut war meme command
async def parnut_showimg(client, message, parameter):
    await message.channel.send(file=File("images/parnut.png"))


# gym boss meme command
async def gymboss_showimg(client, message, parameter):
    await message.channel.send(file=File("images/gym_boss.png"))


# so good meme command
async def sogood_showimg(client, message, parameter):
    await message.channel.send(file=File("images/so_good.png"))


# believable galaxy meme command
async def believable_showimg(client, message, parameter):
    await message.channel.send(file=File("images/believable.jpg"))


# trigger definitions
async def setup(client):

    # flags
    client.register_command('flag', flag_showimg)
    client.register_command('battleflag', battle_flag_showimg)

    # logo
    client.register_command('logo', logo_showimg)

    # other memes
    client.register_command('bhadaba', bhadaba_showimg)
    client.register_command('ASP', asp_showimg)
    client.register_command('landmine', landmine_showimg)
    client.register_command('skimmer', skimmer_showimg)
    client.register_command('staysafe', safe_showimg)
    client.register_command('conquest', conquest_showimg)
    client.register_command('aisling', aisling_showimg)
    client.register_command('biowaste', brabowaste_showimg)
    client.register_command('parnut', parnut_showimg)
    client.register_command('gymboss', gymboss_showimg)
    client.register_command('sogood', sogood_showimg)
    client.register_command('believable', believable_showimg)
