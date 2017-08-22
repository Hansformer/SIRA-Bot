import pendulum

from config import tzone, tformat, admins


# timestamp formatting for console/terminal
def get_time():
    zone = pendulum.timezone(tzone)
    stamp = pendulum.now(zone).strftime(tformat)
    return stamp


def is_admin(fn):
    async def ret_fn(client, message, parameter):
        if message.author.id in admins:
            return await fn(client, message, parameter)
        else:
            raise Exception('Unauthorized')
    return ret_fn
