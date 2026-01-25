import aiohttp


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        api = await resp.json()
        return api
