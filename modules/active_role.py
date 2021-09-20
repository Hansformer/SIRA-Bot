import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('active', 'Toggle your Active Roster role.')
async def active_role_set(ctx: tanjun.abc.Context) -> None:
    role = 424537981731471361
    if role not in ctx.member.role_ids:
        await ctx.respond('The Active Roster is for SIRA members only.')
        return

    active_role = 217630454394650634
    inactive_role = 465324094863179777

    if active_role in ctx.member.role_ids:
        await ctx.member.remove_role(active_role)
        await ctx.member.add_role(inactive_role)
        await ctx.respond('You have been removed from the Active Roster.')
    else:
        await ctx.member.add_role(active_role)
        if inactive_role in ctx.member.role_ids:
            await ctx.member.remove_role(inactive_role)
        await ctx.respond('You have been added to the Active Roster.')


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
