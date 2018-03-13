# flag command
async def flag(client, message, parameter):
    await client.send_file(message.channel, "flag_of_space_ireland.png")


# new battleflag command
async def battleflag(client, message, parameter):
    await client.send_file(message.channel, "battleflag.png")


# logo command
async def logo(client, message, parameter):
    await client.send_file(message.channel, "sira_logo.png")


# exploration HUD cheatsheet command
async def exp_hud(client, message, parameter):
    await client.send_file(message.channel, "exp_hud.png")


# exploration sysmap cheatsheet command
async def exp_sysmap(client, message, parameter):
    await client.send_file(message.channel, "exp_sysmap.jpg")


# Bhadaba :DDD
async def bhadaba(client, message, parameter):
    await client.send_file(message.channel, "Bhadaba.jpg")


# space ira command
async def space_ira(client, message, parameter):
    await client.send_message(message.channel,
                              f'https://www.youtube.com/watch?v=5h7UPVOz6MU')


# Actually useful command, post inara page
async def inara(client, message, parameter):
    await client.send_message(message.channel,
                              f'<:space_ireland:309204831548211201> **SIRA'
                              ' INARA Wing**: <https://inara.cz/wing/1470/>')


# Actually useful command pt. 2
async def recruit_brief(client, message, parameter):
    await client.send_message(message.channel,
                              f':beginner: **SIRA New Recruit Briefing**: '
                              '<https://inara.cz/wing-documents/1470/518/>')


# Actually useful command pt. 3: material traders
async def mat_trader(client, message, parameter):
    await client.send_message(message.channel,
                              f':scales: __**Material Traders Near HQ**__:\n'
                              ':floppy_disk: **Encoded**: Quimper Ring, LHS 21'
                              '\n:gear: **Manufactured**: Barba Ring, LP 355-65'
                              '\n:full_moon: **Raw Materials**: Wedge Hangar, '
                              'LFT 300')


# Actually useful command pt. 4: mining ref
async def mining(client, message, parameter):
    await client.send_message(message.channel,
                              f':pick: **SIRA Mining Reference**: '
                              '<https://inara.cz/wing-documents/1470/864/>')


# Actually useful command pt. 5: territory ref
async def hq_ref(client, message, parameter):
    await client.send_message(message.channel,
                              f'<:space_ireland:309204831548211201> **SIRA '
                              'Territory Reference**: '
                              '<https://inara.cz/wing-documents/1470/517/>')


# trigger definitions
async def setup(client):
    client.register_command('flag', flag)
        for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battleflag)
    client.register_command('logo', logo)
    client.register_command('explore_hud', exp_hud)
    client.register_command('explore_sysmap', exp_sysmap)
    client.register_command('bhadaba', bhadaba)
    for alias in ['spaceira', 'space_ira']:
        client.register_command(alias, space_ira)
    for alias in ['inara', 'wing']:
        client.register_command(alias, inara)
    client.register_command('recruit_brief', recruit_brief)
    client.register_command('mat_trader', mat_trader)
    client.register_command('mining', mining)
    client.register_command('hq_ref', hq_ref)
