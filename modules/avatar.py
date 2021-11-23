import aiofiles
import tanjun

from sirabot.checks import role_check

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('avatar', "Refresh bot's avatar (after changing it in git)")
async def avatar(ctx: tanjun.abc.Context) -> None:
    async with aiofiles.open('images/siraicon.png', mode='rb') as file:
        contents = await file.read()
    await ctx.rest.edit_my_user(avatar=contents)


loader = component.make_loader()
