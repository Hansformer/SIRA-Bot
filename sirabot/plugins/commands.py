import discord
from asyncio import sleep


# nearby material traders command
async def mat_trader_display(client, message, parameter):
    await message.channel.send(':scales: __**Material Traders Near HQ**__:\n'
                               ':floppy_disk: **Encoded**: Quimper Ring, LHS 21'
                               '\n:gear: **Manufactured**: Barba Ring, '
                               'LP 355-65\n:full_moon: **Raw Materials**: '
                               'Wedge Hangar, LFT 300')


# active role tagging command
async def active_role_set(client, message, parameter):
    role = discord.utils.get(message.guild.roles, name="SIRA")
    if role not in message.author.roles:
        await message.channel.send(f'The {message.content[1:]} role is for SIRA'
                                   ' members only.')
        return

    r1 = "Active Roster"
    r2 = "Inactive"
    if message.content == "!inactive":
        temp = r1
        r1 = r2
        r2 = temp
    role = discord.utils.get(message.guild.roles, name=r1)
    role2 = discord.utils.get(message.guild.roles, name=r2)

    if role in message.author.roles:
        await message.channel.send('You already have this role.')
    else:
        await message.author.add_roles(role)
        await sleep(1.5)
        if role2 in message.author.roles:
            await message.author.remove_roles(role2)
        await message.channel.send('Done.')


# powerplay role tagging command
async def lyr_role_set(client, message, parameter):
    role = discord.utils.get(message.guild.roles, name="SIRA")
    if role not in message.author.roles:
        await message.channel.send('The LYR role is for SIRA members only.')
        return
    role = discord.utils.get(message.guild.roles,
                             name="LYR Discount Defence Force")
    if role in message.author.roles:
        await message.author.remove_roles(role)
        await message.channel.send('You have been removed from the LYR roster.')
    else:
        await message.author.add_roles(role)
        await message.channel.send('You have been added to the LYR roster.')


# trigger definitions
async def setup(client):

    # material traders
    for alias in ['mattrade', 'mat_trader', 'mat_traders']:
        client.register_command(alias, mat_trader_display)

    # active/inactive role tagging
    for alias in ['active', 'inactive']:
        client.register_command(alias, active_role_set)

    # lyr role tagging
    for alias in ['LYR', 'lyr']:
        client.register_command(alias, lyr_role_set)
