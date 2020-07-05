from enum import Enum


class Status(Enum):
    snow = 'Snow'
    sleet = 'Sleet'
    hail = 'Hail'
    thunderstorm = 'Thunderstorm'
    heavyRain = 'Heavy Rain'
    lightRain = 'Light Rain'
    showers = 'Showers'
    heavyCloud = 'Heavy Cloud'
    clear = 'Clear'
    lightCloud = 'Light Cloud'
    unknown = 'unknown'

status=Status