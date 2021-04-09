import logging
import pendulum
import discord.utils

from config import TIME_ZONE, TIME_FORMAT, ADMIN_ROLE

logger = logging.getLogger('sirabot')


# timestamp formatting for console/terminal
def get_time():
    zone = pendulum.timezone(TIME_ZONE)
    stamp = pendulum.now(zone).strftime(TIME_FORMAT)
    return stamp


def is_admin(fn):
    async def ret_fn(client, message, parameter):
        if discord.utils.get(message.author.roles, name=ADMIN_ROLE) is not None:
            return await fn(client, message, parameter)
        logger.debug('Permission denied: %s Message: %s', message.author.id, message.content)
    return ret_fn
