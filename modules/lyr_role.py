import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('lyr', 'Toggle your LYR role.')
async def lyr_role_set(ctx: tanjun.abc.Context) -> None:
    role = 424537981731471361
    if role not in ctx.member.role_ids:
        await ctx.respond('The LYR role is for SIRA members only.')
        return

    lyr_role = 314059146645209088
    if lyr_role in ctx.member.role_ids:
        await ctx.member.remove_role(lyr_role)
        await ctx.respond('You have been removed from the LYR roster.')
    else:
        await ctx.member.add_role(lyr_role)
        await ctx.respond('You have been added to the LYR roster.')


loader = component.make_loader()
