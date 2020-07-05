import aiohttp
from config.settings import settings


async def fetch_location_id(session_, url: str, user_location):
    params = {'query': user_location}
    try:
        async with session_.get(url, params=params) as response:
            return await response.json()
    except aiohttp.ClientConnectionError as e:
        return None


async def provide_remote_data(city):
    global city_key
    async with aiohttp.ClientSession(conn_timeout=60) as session:
        content = await fetch_location_id(session, settings.location_url, user_location=city)
        if content:
            data_persisted = dict()
            for x in content:
                city_key = x['woeid']
                data_persisted[city_key] = x
            async with session.get(f'{settings.weather_url}/{city_key}') as response:
                resp = await response.json()
                return resp['consolidated_weather']
        else:
            return None
