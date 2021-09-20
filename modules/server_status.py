import tanjun

from sirabot.utils import fetch

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('status', "Elite's server status according to EDSM.")
async def server_status(ctx: tanjun.abc.Context) -> None:
    api = await fetch('https://www.edsm.net/api-status-v1/elite-server')
    sstatus, smsg = api['type'], api['message']

    msg = 'Something went wrong'
    if sstatus == 'success':
        msg = f'FDev says "{smsg}". :ok_hand:'
    elif sstatus == 'warning':
        msg = f':warning: FDev says "{smsg}".'
    elif sstatus == 'danger':
        msg = f':fire: "{smsg}". Sandro tripped over the server cords again.'

    await ctx.respond(msg)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
