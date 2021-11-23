import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('mattrade', 'Display material traders near HQ.')
async def mat_trader_display(ctx: tanjun.abc.Context) -> None:
    await ctx.respond(':scales: __**Material Traders Near HQ**__:\n'
                      ':floppy_disk: **Encoded**: Quimper Ring, LHS 21\n'
                      ':gear: **Manufactured**: Barba Ring, LP 355-65\n'
                      ':full_moon: **Raw Materials**: Wedge Hangar, LFT 300')


loader = component.make_loader()
