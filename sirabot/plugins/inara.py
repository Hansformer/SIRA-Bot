# inara page command
async def inara(client, message, parameter):
    await client.send_message(message.channel,
                              '<:space_ireland:309204831548211201> **SIRA'
                              ' INARA Wing**: <https://inara.cz/wing/1470/>')


# recruit briefing command
async def recruit_brief(client, message, parameter):
    await client.send_message(message.channel,
                              ':beginner: **SIRA New Recruit Briefing**: '
                              '<https://inara.cz/wing-documents/1470/518/>')


# mining reference command
async def mining(client, message, parameter):
    await client.send_message(message.channel,
                              ':pick: **SIRA Mining Reference**: '
                              '<https://inara.cz/wing-documents/1470/864/>')


# territory reference command
async def hq_ref(client, message, parameter):
    await client.send_message(message.channel,
                              '<:space_ireland:309204831548211201> **SIRA '
                              'Territory Reference**: '
                              '<https://inara.cz/wing-documents/1470/517/>')


# powerplay briefing command
async def pp_brief(client, message, parameter):
    await client.send_message(message.channel,
                              ':tickets: **SIRA Powerplay Briefing**: '
                              '<https://inara.cz/wing-documents/1470/512/>')


# background sim briefing command
async def bgs_brief(client, message, parameter):
    await client.send_message(message.channel,
                              ':bar_chart: **SIRA BGS Briefing**: '
                              '<https://inara.cz/wing-documents/1470/516/>')


# lore and history command
async def lore(client, message, parameter):
    await client.send_message(message.channel,
                              ':book: **SIRA Lore & History**: '
                              '<https://sira.space/#lore>')


# trigger definitions
async def setup(client):
    for alias in ['inara', 'wing']:
        client.register_command(alias, inara)
    client.register_command('recruit_brief', recruit_brief)
    client.register_command('mining', mining)
    client.register_command('hq_ref', hq_ref)
    client.register_command('pp_brief', pp_brief)
    client.register_command('bgs_brief', bgs_brief)
    for alias in ['lore', 'history']:
        client.register_command(alias, lore)
