import aiohttp
import pendulum


# fetch command
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            api = await resp.json()
            return api


# server status command
async def server_status(_client, message, _parameter):
    api = await fetch('https://www.edsm.net/api-status-v1/elite-server')
    sstatus, smsg = api['type'], api['message']

    msg = 'Something went wrong'
    if sstatus == 'success':
        msg = f'FDev says "{smsg}". :ok_hand:'
    elif sstatus == 'warning':
        msg = f':warning: FDev says "{smsg}".'
    elif sstatus == 'danger':
        msg = f':fire: "{smsg}". Sandro tripped over the server cords again.'

    await message.channel.send(msg)


# faction info command
async def system_inf(_client, message, parameter):
    api = await fetch(
        f'https://www.edsm.net/api-system-v1/factions?systemName={parameter}')
    if api:
        text = f"```{api['name']} Influence Overview```"
        for faction in api['factions']:
            if faction['influence'] != 0:
                text += process_faction_inf(api, faction)

        text += pendulum.from_timestamp(api['factions'][0]
                                        ['lastUpdate']).to_rfc2822_string()
        await message.channel.send(text)
    else:
        await message.channel.send("I can't find that, senpai.")


async def process_faction_inf(api, faction):
    sira_name = 'SIRA Incorporated'
    ally_names = ['Iridium Wing', 'CROSS Corp', 'Pan Galactic Mining Corp.',
                  'Sirius Special Forces', 'Wrecking Crew', 'Aseveljet']
    enemy_names = ['EXO', 'The Fatherhood']
    text = ''

    if api['controllingFaction']['id'] == faction['id']:
        text += f":crown: **{faction['name']}**"
    else:
        text += f"**{faction['name']}**"

    if faction['isPlayer']:
        if faction['name'] == sira_name:
            text += " <:space_ireland:309204831548211201> "
        elif faction['name'] in ally_names:
            text += " :green_heart: "
        elif faction['name'] in enemy_names:
            text += " :skull: "
        else:
            text += " :joystick: "
    text += f": {faction['influence']:.1%}"

    if faction['state'] != 'None':
        text += f" ({faction['state']})"
    text += "\n"

    if faction['pendingStates']:
        text += ":fast_forward: __Pending__:"
        for pending_state in faction['pendingStates']:
            text += f" {pending_state['state']} "
            if pending_state['trend'] >= 1:
                text += ":small_red_triangle:"
            elif pending_state['trend'] == 0:
                text += "(-)"
            else:
                text += ":small_red_triangle_down:"
            text += ";"
        text += "\n"

    if faction['recoveringStates']:
        text += ":twisted_rightwards_arrows: __Recovering__:"
        for recovering_state in faction['recoveringStates']:
            text += f" {recovering_state['state']} "
            if recovering_state['trend'] >= 1:
                text += ":small_red_triangle:"
            elif recovering_state['trend'] == 0:
                text += "(-)"
            else:
                text += ":small_red_triangle_down:"
            text += ";"
        text += "\n"

    text += f":classical_building: `{faction['allegiance']}, " \
            f"{faction['government']}`\n" \
            "---\n"

    return text


# traffic report command
async def traffic_report(_client, message, parameter):
    api = await fetch(
        f'https://www.edsm.net/api-system-v1/traffic?systemName={parameter}')

    if api:
        traffic = api['traffic']
        text = f"```{api['name']} EDSM Traffic Report```" \
               f"Last 24 Hours: {traffic['day']}\n" \
               f"Last 7 Days: {traffic['week']}\n" \
               f"All Time: {traffic['total']}"
        # for ship in api['breakdown']:
        #    text += ship
        await message.channel.send(text)
    else:
        await message.channel.send("I can't find that, senpai.")


# trigger definitions
async def setup(client):
    for alias in ['server', 'status']:
        client.register_command(alias, server_status)
    client.register_command('sysinf', system_inf)
    client.register_command('traffic', traffic_report)
