import click
import time, random
from repo.app_repo import AppRepository
import asyncio
from models.weather import Weather
import dateutil.parser
import datetime
from ascify import runner
import os
from config.settings import settings

app_repo = AppRepository()


def location_finder():
    return app_repo.location_finder()


async def main():
    weather_model = Weather()
    tomorrow_data = Weather()
    day_after_tomorrow = Weather()
    location = location_finder() or settings.default_location

    data = await app_repo.get_data(city_name=location)
    if data:
        # we need to  create three objects of weather model
        weather_model.set_location = location
        raw_date = data[0]['created']
        formatted_date = datetime.datetime.strftime(dateutil.parser.parse(raw_date), '%b %d %Y, %H:%M:%S')
        weather_model.set_created_data = formatted_date
        weather_model.set_minimum_temp = round(data[0]['min_temp'], 1)
        weather_model.set_temp = round(data[0]['the_temp'], 1)
        weather_model.set_maximum_temp = round(data[0]['max_temp'], 1)
        weather_model.set_weather_state = data[0]['weather_state_name']
        weather_model.set_pressure = data[0]['air_pressure']
        weather_model.set_humidity = data[0]['humidity']
        weather_model.set_predictability = data[0]['predictability']
        weather_model.set_applicability_date = data[0]['applicable_date']
        weather_model.set_weather_abbr = app_repo.set_weather_state_abbr(data[0]['weather_state_abbr'])

        # Tomorrow
        tomorrow_data.set_location = location
        raw_date = data[1]['created']
        formatted_date = datetime.datetime.strftime(dateutil.parser.parse(raw_date), '%b %d %Y, %H:%M:%S')
        tomorrow_data.set_created_data = formatted_date
        tomorrow_data.set_minimum_temp = round(data[1]['min_temp'], 1)
        tomorrow_data.set_temp = round(data[1]['the_temp'], 1)
        tomorrow_data.set_maximum_temp = round(data[1]['max_temp'], 1)
        tomorrow_data.set_weather_state = data[1]['weather_state_name']
        tomorrow_data.set_pressure = data[1]['air_pressure']
        tomorrow_data.set_humidity = data[1]['humidity']
        tomorrow_data.set_predictability = data[1]['predictability']
        tomorrow_data.set_applicability_date = data[1]['applicable_date']
        tomorrow_data.set_weather_abbr = app_repo.set_weather_state_abbr(data[1]['weather_state_abbr'])

        # Tomorrow but one
        day_after_tomorrow.set_location = location
        raw_date = data[2]['created']
        formatted_date = datetime.datetime.strftime(dateutil.parser.parse(raw_date), '%b %d %Y, %H:%M:%S')
        day_after_tomorrow.set_created_data = formatted_date
        day_after_tomorrow.set_minimum_temp = round(data[2]['min_temp'], 1)
        day_after_tomorrow.set_temp = round(data[2]['the_temp'], 1)
        day_after_tomorrow.set_maximum_temp = round(data[2]['max_temp'], 1)
        day_after_tomorrow.set_weather_state = data[0]['weather_state_name']
        day_after_tomorrow.set_pressure = data[2]['air_pressure']
        day_after_tomorrow.set_humidity = data[2]['humidity']
        day_after_tomorrow.set_predictability = data[2]['predictability']
        day_after_tomorrow.set_applicability_date = data[2]['applicable_date']
        day_after_tomorrow.set_weather_abbr = app_repo.set_weather_state_abbr(data[2]['weather_state_abbr'])

        click.secho(click.style(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ weather updates ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
            fg='black', bold=True))
        click.secho(click.style(weather_model.location.title(), bold=True, fg='green'))
        print('----------------------------------')
        print()
        # Today
        click.secho(click.secho('Today', fg='bright_blue'))

        if weather_model.weather_state_abbr.lightRain or weather_model.weather_state_abbr.lightRain or weather_model.weather_state_abbr.showers:
            runner(os.getcwd() + '/rainy.png')
        elif weather_model.weather_state_abbr.clear or weather_model.weather_state_abbr.lightCloud:
            runner(os.getcwd() + '/clear.png')
        elif weather_model.weather_state_abbr.hail or weather_model.weather_state_abbr.snow or weather_model.weather_state_abbr.sleet:
            runner(os.getcwd() + '/snow.png')
        elif weather_model.weather_state_abbr.heavyCloud:
            runner(os.getcwd() + '/cloudy.png')
        else:
            runner(os.getcwd() + '/clear.png')
        print()
        click.secho(click.style('Weather state', fg='green', bold=True))
        print(f'{weather_model.weather_state.title()}')
        print(f'Max:{weather_model.max_temp} Celsius')
        print(f'Min:{weather_model.min_temp} Celsius')
        click.secho(click.style('Humidity', fg='green', bold=True))
        print(f'{weather_model.humidity}%')
        click.secho(click.style('Pressure', fg='green', bold=True))
        print(f'{weather_model.pressure}mb')
        click.secho(click.style('Confidence', fg='green', bold=True))
        print(f'{weather_model.predictability}%')

        # Tomorrow
        print()
        click.secho(click.secho('Tomorrow', fg='bright_blue'))
        print('----------------------------------')
        if tomorrow_data.weather_state_abbr.lightRain or tomorrow_data.weather_state_abbr.lightRain or tomorrow_data.weather_state_abbr.showers:
            runner(os.getcwd() + '/rainy.png')
        elif tomorrow_data.weather_state_abbr.clear or tomorrow_data.weather_state_abbr.lightCloud:
            runner(os.getcwd() + '/clear.png')
        elif tomorrow_data.weather_state_abbr.hail or tomorrow_data.weather_state_abbr.snow or tomorrow_data.weather_state_abbr.sleet:
            runner(os.getcwd() + '/snow.png')
        elif tomorrow_data.weather_state_abbr.heavyCloud:
            runner(os.getcwd() + '/cloudy.png')
        else:
            runner(os.getcwd() + '/clear.png')
        print()
        click.secho(click.style('Weather state', fg='green', bold=True))
        print(f'{tomorrow_data.weather_state.title()}')
        print(f'Max:{tomorrow_data.max_temp} Celsius')
        print(f'Min:{tomorrow_data.min_temp} Celsius')
        click.secho(click.style('Humidity', fg='green', bold=True))
        print(f'{tomorrow_data.humidity}%')
        click.secho(click.style('Pressure', fg='green', bold=True))
        print(f'{tomorrow_data.pressure}mb')
        click.secho(click.style('Confidence', fg='green', bold=True))
        print(f'{tomorrow_data.predictability}%')

        # Day after tomorrow
        print()
        click.secho(click.secho(f'Day after tomorrow {day_after_tomorrow.applicability_date}', fg='bright_blue'))
        click.echo('--------------------------------------------------')
        if day_after_tomorrow.weather_state_abbr.lightRain or day_after_tomorrow.weather_state_abbr.lightRain or day_after_tomorrow.weather_state_abbr.showers:
            runner(os.getcwd() + '/rainy.png')
        elif day_after_tomorrow.weather_state_abbr.clear or day_after_tomorrow.weather_state_abbr.lightCloud:
            runner(os.getcwd() + '/clear.png')
        elif day_after_tomorrow.weather_state_abbr.hail or day_after_tomorrow.weather_state_abbr.snow or day_after_tomorrow.weather_state_abbr.sleet:
            runner(os.getcwd() + '/snow.png')
        elif day_after_tomorrow.weather_state_abbr.heavyCloud:
            runner(os.getcwd() + '/cloudy.png')
        else:
            runner(os.getcwd() + '/clear.png')
        print()
        click.secho(click.style('Weather state', fg='green', bold=True))
        print(f'{day_after_tomorrow.weather_state.title()}')
        print(f'Max:{day_after_tomorrow.max_temp} Celsius')
        print(f'Min:{day_after_tomorrow.min_temp} Celsius')
        click.secho(click.style('Humidity', fg='green', bold=True))
        print(f'{day_after_tomorrow.humidity}%')
        click.secho(click.style('Pressure', fg='green', bold=True))
        print(f'{day_after_tomorrow.pressure}mb')
        click.secho(click.style('Confidence', fg='green', bold=True))
        print(f'{day_after_tomorrow.predictability}%')
        click.secho(click.style('Data last updated',fg='green',bold=True))
        print(formatted_date)
    else:
        print("Well this is embarrassing.The city\'s weather data your are looking for is not locally available & "
              "could not be loaded from the servers.Here are some solutions: Check your network "
              "connection and try again (-:")


@click.command()
def main_command():
    with click.progressbar(length=5000, width=0, show_percent=False, label='working please wait',
                           show_eta=False, fill_char=click.style('#',
                                                                 fg='magenta')) as bar:
        for item in bar:
            time.sleep(0.001 * random.random())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == '__main__':
    main_command()
