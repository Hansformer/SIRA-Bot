from hikari.presences import Activity
import tanjun

from sirabot.checks import role_check

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('vision', 'V I S I O N')
async def vision(ctx: tanjun.abc.Context) -> None:
    await ctx.shards.update_presence(afk=False, activity=Activity(name='V I S I O N'))
    await ctx.respond("I have been V I S I O N'd. <:vision_intensifies:332951986645499904>")


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
