import discord


# nearby material traders command
async def mat_trader_display(client, message, parameter):
    await client.send_message(message.channel,
                              ':scales: __**Material Traders Near HQ**__:\n'
                              ':floppy_disk: **Encoded**: Quimper Ring, LHS 21'
                              '\n:gear: **Manufactured**: Barba Ring, LP 355-65'
                              '\n:full_moon: **Raw Materials**: Wedge Hangar, '
                              'LFT 300')


# active role tagging command
async def active_role_set(client, message, parameter):
    role = discord.utils.get(message.server.roles, name="SIRA")
    if role not in message.author.roles:
        await client.send_message(message.channel,
                                  'The active role is for SIRA members only.')
        return
    role = discord.utils.get(message.server.roles, name="Active Roster")
    role2 = discord.utils.get(message.server.roles, name="Inactive")
    if role in message.author.roles:
        await client.send_message(message.channel,
                                 'You already have this role.')
    else:
        await client.add_roles(message.author, role)
        if role2 in message.author.roles:
            await client.remove_roles(message.author, role2)
        await client.send_message(message.channel, 'Done.')


# inactive role tagging command
async def inactive_role_set(client, message, parameter):
    role = discord.utils.get(message.server.roles, name="SIRA")
    if role not in message.author.roles:
        await client.send_message(message.channel,
                                  'The inactive role is for SIRA members only.')
        return
    role = discord.utils.get(message.server.roles, name="Active Roster")
    role2 = discord.utils.get(message.server.roles, name="Inactive")
    if role2 in message.author.roles:
        await client.send_message(message.channel,
                                 'You already have this role.')
    else:
        await client.add_roles(message.author, role2)
        if role in message.author.roles:
            await client.remove_roles(message.author, role)
        await client.send_message(message.channel, 'Done.')


# powerplay role tagging command
async def lyr_role_set(client, message, parameter):
    role = discord.utils.get(message.server.roles, name="SIRA")
    if role not in message.author.roles:
        await client.send_message(message.channel,
                                  'The LYR role is for SIRA members only.')
        return
    role = discord.utils.get(message.server.roles,
                             name="LYR Discount Defence Force")
    if role in message.author.roles:
        await client.remove_roles(message.author, role)
        await client.send_message(message.channel,
                                  'You have been removed from the LYR roster.')
    else:
        await client.add_roles(message.author, role)
        await client.send_message(message.channel,
                                  'You have been added to the LYR roster.')


# trigger definitions
async def setup(client):

    # material traders
    for alias in ['mattrade', 'mat_trader', 'mat_traders']:
        client.register_command(alias, mat_trader_display)

    # active/inactive role tagging
    client.register_command('active', active_role_set)
    client.register_command('inactive', inactive_role_set)

    # lyr role tagging
    for alias in ['LYR', 'lyr']:
        client.register_command(alias, lyr_role_set)
