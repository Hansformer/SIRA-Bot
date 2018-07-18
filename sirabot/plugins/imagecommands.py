# flag command
async def flag_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/flag_of_space_ireland.png")


# new battleflag command
async def battle_flag_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/battleflag.png")


# logo command
async def logo_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/sira_logo.png")


# exploration HUD cheatsheet command
async def explore_hud_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/exp_hud.png")


# exploration sysmap cheatsheet command
async def explore_sysmap_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/exp_sysmap.jpg")


# Bhadaba! meme command
async def bhadaba_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/Bhadaba.jpg")


# asp meme command
async def asp_showimg(client, message, parameter):
    await client.send_file(message.channel, "images/ASP.png")


# trigger definitions
async def setup(client):

    # flags
    client.register_command('flag', flag_showimg)
    for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battle_flag_showimg)

    # logo
    client.register_command('logo', logo)

    # exploration references
    client.register_command('explore_hud', exp_hud)
    for alias in ['explore_sysmap', 'explore_map']:
        client.register_command(alias, exp_sysmap)

    # other memes
    client.register_command('bhadaba', bhadaba)
    client.register_command('ASP', asp)
