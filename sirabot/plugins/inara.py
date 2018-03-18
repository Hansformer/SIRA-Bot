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


# mining reference
async def mining(client, message, parameter):
    await client.send_message(message.channel,
                              f':pick: **SIRA Mining Reference**: '
                              '<https://inara.cz/wing-documents/1470/864/>')


# territory reference
async def hq_ref(client, message, parameter):
    await client.send_message(message.channel,
                              f'<:space_ireland:309204831548211201> **SIRA '
                              'Territory Reference**: '
                              '<https://inara.cz/wing-documents/1470/517/>')


# powerplay briefing
async def pp_brief(client, message, parameter):
    await client.send_message(message.channel,
                              f':tickets: **SIRA Powerplay Briefing**: '
                              '<https://inara.cz/wing-documents/1470/512/>')


# background sim briefing
async def bgs_brief(client, message, parameter):
    await client.send_message(message.channel,
                              f':bar_chart: **SIRA BGS Briefing**: '
                              '<https://inara.cz/wing-documents/1470/516/>')


# background sim briefing
async def lore(client, message, parameter):
    await client.send_message(message.channel,
                              f':book: **SIRA Lore & History**: '
                              '<https://inara.cz/wing-documents/1470/424/>')


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