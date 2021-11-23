from hikari.presences import Activity
import tanjun

from sirabot.checks import role_check

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('idle', '...')
async def idle(ctx: tanjun.abc.Context) -> None:
    await ctx.shards.update_presence(afk=True, activity=Activity(name='with live wires'))
    await ctx.respond('...')


loader = component.make_loader()
