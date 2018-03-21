import aiohttp


# fetch command
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            api = await resp.json()
            return api


# server status command
async def server(client, message, parameter):
    api = await fetch('https://www.edsm.net/api-status-v1/elite-server')
    sstatus, smsg = api['type'], api['message']

    msg = 'Something went wrong'
    if sstatus == 'success':
        msg = f'FDev says "{smsg}". :ok_hand:'
    elif sstatus == 'warning':
        msg = f':warning: FDev says "{smsg}".'
    elif sstatus == 'danger':
        msg = f':fire: "{smsg}". Sandro tripped over the server cords again.'

    await client.send_message(message.channel, msg)


# faction info command
async def system_inf(client, message, parameter):
    api = await fetch(
        f'https://www.edsm.net/api-system-v1/factions?systemName={parameter}')

    if api:
        text = f"```{api['name']} Faction Overview```"
        for faction in api['factions']:
            if faction['influence'] != 0:
                if api['controllingFaction']['id'] == faction['id']:
                    text += f":crown: **{faction['name']}**"
                else:
                    text += f"**{faction['name']}**"
                if faction['isPlayer']:
                    text += f" *(Player)*"
                text += f": {faction['influence']:.1%}"
                if faction['state'] != 'None':
                    text += f" ({faction['state']})"
                text += f"\n"
                if faction['pendingStates']:
                    text += f">> __Pending__: "
                    for pendingState in faction['pendingStates']:
                        text += f"{pendingState['state']} "
                        if pendingState['trend'] >= 1:
                            text += f":small_red_triangle:"
                        if pendingState['trend'] <= 0:
                            text += f":small_red_triangle_down:"
                        text += f";"
                    text += f"\n"
                text += f">> `{faction['allegiance']}, " \
                        f"{faction['government']}`\n"

        await client.send_message(message.channel, text)
    else:
        await client.send_message(message.channel, 'invalid')


# trigger definitions
async def setup(client):
    for alias in ['server', 'status']:
        client.register_command(alias, server)
    for alias in ['sys_bgs', 'sysbgs', 'sys_inf', 'sysinf']:
        client.register_command(alias, system_inf)
