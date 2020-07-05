from data_sources import local_data_source
from data_sources import remote_data_source
import ipinfo
from typing import Optional
from models.status import status

class AppRepository:
    def __init__(self):
        self._data = dict()

    async def get_data(self, city_name: str):
        try:
            remote_data = await remote_data_source.provide_remote_data(city=city_name)
            if remote_data is not None:
                local_copy = local_data_source.provide_local_data()
                if local_copy is not None :
                    if city_name in local_copy:
                        del local_copy[city_name]
                        local_copy[city_name] = remote_data
                        self._data = local_copy
                else:
                    self._data[city_name]= remote_data
                local_data_source.persist_local_data(self._data)
                return self._data[city_name]
            else:
                self._data = local_data_source.provide_local_data()
                if city_name in self._data:
                    return self._data[city_name]
                else:
                    return None
        except IOError as e:
            self._data = local_data_source.provide_local_data()
            if city_name in self._data:
                return self._data[city_name]
            else:
                return None

    @staticmethod
    def location_finder()->Optional[str]:
        try:
<<<<<<< HEAD
            access_token = '' # get your token from ipinfo
=======
            access_token = '' # put your access token go to ipinfo.com to get the access token
>>>>>>> c6431e7330ad31cbee5fb5d061a23986f215dca7
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails()
            return details.city
        except Exception as e:
            return None

    @staticmethod
    def set_weather_state_abbr(state: str):
        if state == 'lr':
            return status.lightRain
        elif state == 't':
            return status.thunderstorm
        elif state == 'h':
            return status.hail
        elif state == 'lc':
            return status.lightCloud
        elif state== 'hr':
            return status.heavyRain
        elif state == 'sn':
            return status.snow
        elif state == 's1':
            return status.sleet
        else:
            return status.unknown


