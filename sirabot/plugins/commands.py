# flag command
async def flag(client, message, parameter):
    await client.send_file(message.channel, "images/flag_of_space_ireland.png")


# new battleflag command
async def battle_flag(client, message, parameter):
    await client.send_file(message.channel, "images/battleflag.png")


# logo command
async def logo(client, message, parameter):
    await client.send_file(message.channel, "images/sira_logo.png")


# exploration HUD cheatsheet command
async def exp_hud(client, message, parameter):
    await client.send_file(message.channel, "images/exp_hud.png")


# exploration sysmap cheatsheet command
async def exp_sysmap(client, message, parameter):
    await client.send_file(message.channel, "images/exp_sysmap.jpg")


# Bhadaba :DDD
async def bhadaba(client, message, parameter):
    await client.send_file(message.channel, "images/Bhadaba.jpg")


# space ira command
async def space_ira(client, message, parameter):
    await client.send_message(message.channel,
                              f'https://www.youtube.com/watch?v=5h7UPVOz6MU')


# material traders
async def mat_trader(client, message, parameter):
    await client.send_message(message.channel,
                              f':scales: __**Material Traders Near HQ**__:\n'
                              ':floppy_disk: **Encoded**: Quimper Ring, LHS 21'
                              '\n:gear: **Manufactured**: Barba Ring, LP 355-65'
                              '\n:full_moon: **Raw Materials**: Wedge Hangar, '
                              'LFT 300')


# help/readme
async def bot_help(client, message, parameter):
    await client.send_message(message.channel,
                              f':robot: **SIRA Bot Help**: <https://github.com/'
                              'Hansformer/SIRA-Bot/blob/master/README.md>')


# trigger definitions
async def setup(client):
    client.register_command('flag', flag)
    for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battle_flag)
    client.register_command('logo', logo)
    client.register_command('explore_hud', exp_hud)
    client.register_command('explore_sysmap', exp_sysmap)
    client.register_command('bhadaba', bhadaba)
    for alias in ['spaceira', 'space_ira']:
        client.register_command(alias, space_ira)
    client.register_command('mat_trader', mat_trader)
    client.register_command('help', bot_help)
