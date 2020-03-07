# website link command
async def site_link(client, message, parameter):
    await message.channel.send(':globe_with_meridians: **SIRA Website**: '
                               'https://sira.space/')


# lore and history command
async def lore_link(client, message, parameter):
    await message.channel.send(':book: **SIRA History/Lore**: '
                               '<https://sira.space/?page=lore>')


# inara page command
async def inara_link(client, message, parameter):
    await message.channel.send('<:space_ireland:309204831548211201> **INARA'
                               ' Squadron Page**: '
                               '<https://inara.cz/squadron/1470/>')


# bot help/readme command
async def bot_help_link(client, message, parameter):
    await message.channel.send(':robot: **SIRA-Bot Help**: <https://github.com/'
                               'Hansformer/SIRA-Bot#helpcommands>')


# space ira video command
async def space_ira_ytlink(client, message, parameter):
    await message.channel.send('https://www.youtube.com/watch?v=5h7UPVOz6MU')


# territory reference command
async def territory_link(client, message, parameter):
    await message.channel.send('<:space_ireland:309204831548211201> **SIRA '
                               'Territory Reference**: '
                               '<https://inara.cz/squadron-documents/1470/517/>')


# mining reference command
async def mining_link(client, message, parameter):
    await message.channel.send(':pick: **SIRA Mining Reference**: '
                               '<https://inara.cz/squadron-documents/1470/864/>')


# background sim information command
async def bgs_brief(client, message, parameter):
    await message.channel.send(':bar_chart: **BGS Information**: '
                               '<https://forums.frontier.co.uk/showthread.php/'
                               '400110-Don-t-Panic-BGS-guides-and-help>')


# trigger definitions
async def setup(client):

    # website link
    for alias in ['website', 'site', 'link']:
        client.register_command(alias, site_link)

    # history/lore link
    for alias in ['lore', 'history']:
        client.register_command(alias, lore_link)

    # inara wing page link
    for alias in ['inara', 'wing', 'squad']:
        client.register_command(alias, inara_link)

    # help/readme link
    client.register_command('help', bot_help_link)

    # space ira video link
    client.register_command('spaceira', space_ira_ytlink)

    # territory reference links
    client.register_command('territory', territory_link)
    client.register_command('mining', mining_link)

    client.register_command('bgs', bgs_brief)
