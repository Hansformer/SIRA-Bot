import logging
import pendulum
import discord.utils

from config import tzone, tformat, adminrole

logger = logging.getLogger('sirabot')


# timestamp formatting for console/terminal
def get_time():
    zone = pendulum.timezone(tzone)
    stamp = pendulum.now(zone).strftime(tformat)
    return stamp


def is_admin(fn):
    async def ret_fn(client, message, parameter):
        if discord.utils.get(message.author.roles, name=adminrole) is not None:
            return await fn(client, message, parameter)
        logger.debug(f'Permission denied: %s Message: %s', message.author.id, message.content)
    return ret_fn
