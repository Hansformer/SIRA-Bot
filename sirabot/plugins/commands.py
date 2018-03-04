# flag command
async def flag(client, message, parameter):
    await client.send_file(message.channel, "flag_of_space_ireland.png")


# new battleflag command
async def battleflag(client, message, parameter):
    await client.send_file(message.channel, "battleflag.png")


# logo command
async def logo(client, message, parameter):
    await client.send_file(message.channel, "sira_logo.png")


# space ira command
async def space_ira(client, message, parameter):
    await client.send_message(message.channel,
                              f'https://www.youtube.com/watch?v=5h7UPVOz6MU')


# Actually useful command, post inara page
async def inara(client, message, parameter):
    await client.send_message(message.channel,
                              f'<https://inara.cz/wing/1470/>')


# Actually useful command pt. 2
async def recruitbrief(client, message, parameter):
    await client.send_message(message.channel,
                              f'<https://inara.cz/wing-documents/1470/518/>')


# trigger definitions
async def setup(client):
    for alias in ['spaceira', 'space_ira']:
        client.register_command(alias, space_ira)
    client.register_command('flag', flag)
    client.register_command('logo', logo)
    for alias in ['battleflag', 'battle_flag']:
        client.register_command(alias, battleflag)
    client.register_command('inara', inara)
    client.register_command('recruit', recruitbrief)