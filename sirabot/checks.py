from tanjun import abc as tanjun_abc

import config


async def role_check(ctx: tanjun_abc.Context) -> bool:
    result = config.ADMIN_ROLE in ctx.member.role_ids

    return result
