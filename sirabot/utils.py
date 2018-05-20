import logging
import pendulum

from config import tzone, tformat, adminrole

logger = logging.getLogger('sirabot')


# timestamp formatting for console/terminal
def get_time():
    zone = pendulum.timezone(tzone)
    stamp = pendulum.now(zone).strftime(tformat)
    return stamp


def is_admin(fn):
    async def ret_fn(client, message, parameter):
        if adminrole in message.author.roles:
            return await fn(client, message, parameter)
        else:
            logger.debug(f'Permission denied: {message.author.id} '
                         f'Roles: {message.author.roles} '
                         f'Message: {message.content}')
    return ret_fn
