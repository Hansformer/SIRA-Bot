# website link command
async def site_link(client, message, parameter):
    await client.send_message(message.channel,
                              ':globe_with_meridians: **SIRA Website**: '
                              '<https://sira.space/')


# lore and history command
async def lore_link(client, message, parameter):
    await client.send_message(message.channel,
                              ':book: **SIRA Lore & History**: '
                              '<https://sira.space/?page=lore>')


# inara page command
async def inara_link(client, message, parameter):
    await client.send_message(message.channel,
                              '<:space_ireland:309204831548211201> **SIRA'
                              ' INARA Wing**: <https://inara.cz/wing/1470/>')


# bot help/readme command
async def bot_help_link(client, message, parameter):
    await client.send_message(message.channel,
                              ':robot: **SIRA-Bot Help**: <https://github.com/'
                              'Hansformer/SIRA-Bot#helpcommands>')


# space ira video command
async def space_ira_ytlink(client, message, parameter):
    await client.send_message(message.channel,
                              'https://www.youtube.com/watch?v=5h7UPVOz6MU')


# territory reference command
async def territory_link(client, message, parameter):
    await client.send_message(message.channel,
                              '<:space_ireland:309204831548211201> **SIRA '
                              'Territory Reference**: '
                              '<https://inara.cz/wing-documents/1470/517/>')


# mining reference command
async def mining_link(client, message, parameter):
    await client.send_message(message.channel,
                              ':pick: **SIRA Mining Reference**: '
                              '<https://inara.cz/wing-documents/1470/864/>')


# trigger definitions
async def setup(client):

    # website link
    for alias in ['website', 'link']:
        client.register_command(alias, site_link)

    # history/lore link
    for alias in ['lore', 'history']:
        client.register_command(alias, lore_link)

    # inara wing page link
    for alias in ['inara', 'wing']:
        client.register_command(alias, inara_link)

    # help/readme link
    client.register_command('help', bot_help_link)

    # space ira video link
    for alias in ['spaceira', 'space_ira']:
        client.register_command(alias, space_ira_ytlink)

    # territory reference links
    client.register_command('hq_ref', territory_link)
    client.register_command('mining', mining_link)
