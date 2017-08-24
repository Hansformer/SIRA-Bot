import aiohttp


# get server status from EDSM API
async def check_server():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://www.edsm.net/api-status-v1/elite-server'
                ) as resp:
            api = await resp.json()
            return api['type'], api['message']


async def server(client, message, parameter):
    sstatus, smsg = await check_server()
    if sstatus == 'success':
        await client.send_message(message.channel,
                                  f'FDev says "{smsg}". :ok_hand:')
    elif sstatus == 'warning':
        await client.send_message(message.channel,
                                  f':warning: FDev says "{smsg}".')
    elif sstatus == 'danger':
        await client.send_message(message.channel,
                                  f':fire: "{smsg}". Sandro tripped over the'
                                  ' server cords again.')


async def flag(client, message, parameter):
    await client.send_file(message.channel, "flag_of_space_ireland.png")


async def logo(client, message, parameter):
    await client.send_file(message.channel, "sira_logo.png")


async def setup(client):
    for alias in ['server', 'status']:
        client.register_command(alias, server)
    client.register_command('flag', flag)
    client.register_command('logo', logo)
