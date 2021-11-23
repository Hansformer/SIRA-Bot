import time
import tanjun

from sirabot.checks import role_check

component = tanjun.Component()


@component.with_slash_command
@tanjun.with_check(role_check)
@tanjun.as_slash_command('ping', 'Info on latency to Discord')
async def ping(ctx: tanjun.abc.Context) -> None:
    start_time = time.perf_counter()
    await ctx.respond(content='Nyaa master!!!')
    time_taken = (time.perf_counter() - start_time) * 1_000
    heartbeat_latency = ctx.shards.heartbeat_latency * 1_000 if ctx.shards else float('NAN')
    await ctx.edit_last_response(f'PONG\n - REST: {time_taken:.0f}ms\n - Gateway: {heartbeat_latency:.0f}ms')


loader = component.make_loader()
