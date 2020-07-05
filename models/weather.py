from datetime import datetime


class Weather:
    def __init__(self):
        self._location = " "
        self._weather_state_abbr = 'c'
        self._created = ""
        self._temp = 0.0 # 25 Celsius
        self._weather_state = ''
        self._min_temp = 0.0  # 28 *Celsius
        self._max_temp = 0.0  # 23 Celsius
        self._predictability = 0  # 61 %
        self._humidity = 0  # 70%
        self._pressure = 0  # 1015 mb
        self._applicability_date = " "
        self._last_updated = datetime.now()

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def set_pressure(self, value):
        self._pressure = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def set_humidity(self, value):
        self._humidity = value

    @property
    def applicability_date(self):
        return self._applicability_date

    @applicability_date.setter
    def set_applicability_date(self, value):
        self._applicability_date = value

    @property
    def predictability(self):
        return self._predictability

    @predictability.setter
    def set_predictability(self, value):
        self._predictability = value

    @property
    def location(self):
        return self._location

    @location.setter
    def set_location(self, new_location):
        assert isinstance(new_location, str), "The location must be a string"

        self._location = new_location

    @property
    def weather_state(self):
        return self._weather_state

    @weather_state.setter
    def set_weather_state(self, state):
        self._weather_state = state

    @property
    def max_temp(self):
        return self._max_temp

    @max_temp.setter
    def set_maximum_temp(self, temp):
        self._max_temp = temp

    @property
    def weather_state_abbr(self):
        return self._weather_state_abbr

    @weather_state_abbr.setter
    def set_weather_abbr(self, status):
        self._weather_state_abbr = status

    @property
    def created(self):
        return self._created

    @created.setter
    def set_created_data(self, created: str):
        self._created = created

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def set_temp(self, temp: float):
        self._temp = temp

    @property
    def min_temp(self):
        return self._min_temp

    @min_temp.setter
    def set_minimum_temp(self, temp: float):
        self._min_temp = temp

    @property
    def last_updated(self):
        return self._last_updated
