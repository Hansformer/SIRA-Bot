import discord

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


# Bhadaba! command
async def bhadaba(client, message, parameter):
    await client.send_file(message.channel, "images/Bhadaba.jpg")


# asp meme command
async def asp(client, message, parameter):
    await client.send_file(message.channel, "images/ASP.png")


# space ira command
async def space_ira(client, message, parameter):
    await client.send_message(message.channel,
                              'https://www.youtube.com/watch?v=5h7UPVOz6MU')


# nearby material traders command
async def mat_trader(client, message, parameter):
    await client.send_message(message.channel,
                              ':scales: __**Material Traders Near HQ**__:\n'
                              ':floppy_disk: **Encoded**: Quimper Ring, LHS 21'
                              '\n:gear: **Manufactured**: Barba Ring, LP 355-65'
                              '\n:full_moon: **Raw Materials**: Wedge Hangar, '
                              'LFT 300')


# bot help/readme command
async def bot_help(client, message, parameter):
    await client.send_message(message.channel,
                              ':robot: **SIRA-Bot Help**: <https://github.com/'
                              'Hansformer/SIRA-Bot#helpcommands>')


# active role tagging
async def active_role_set(client, message, parameter):
    role = discord.utils.get(message.server.roles, name="SIRA")
    if role not in message.author.roles:
        await client.send_message(message.channel, "The active role is for SIRA members only.")
        return
    role = discord.utils.get(message.server.roles, name="Active Roster")
    if role in message.author.roles:
        await client.send_message(message.channel, 'You already have this role.')
    else:
        await client.add_roles(message.author, role)
        await client.send_message(message.channel, 'Done.')


# inactive role tagging
async def inactive_role_set(client, message, parameter):
    role = discord.utils.get(message.server.roles, name="Active Roster")
    if role not in message.author.roles:
        await client.send_message(message.channel, 'Cannot remove a role you do not have.')
    else:
        await client.remove_roles(message.author, role)
        await client.send_message(message.channel, 'Done.')


# trigger definitions
async def setup(client):
    client.register_command('flag', flag)
    for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battle_flag)
    client.register_command('logo', logo)
    client.register_command('explore_hud', exp_hud)
    client.register_command('explore_sysmap', exp_sysmap)
    client.register_command('bhadaba', bhadaba)
    client.register_command('ASP', asp)
    for alias in ['spaceira', 'space_ira']:
        client.register_command(alias, space_ira)
    for alias in ['mattrade', 'mat_trader']:
        client.register_command(alias, mat_trader)
    client.register_command('help', bot_help)
    client.register_command('active', active_role_set)
    client.register_command('inactive', inactive_role_set)
