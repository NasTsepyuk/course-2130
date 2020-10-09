import requests
from datetime import datetime
from collections import Counter


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        self.api_key = api_key


    def get_current_weather(self, lat, lon):

        """
            TODO: return a weather for current day
            {
                'name': name (time zone name),
                'current_time': current time,  # форматируйте время
                'condition': condition (check the api description),
                'temp': f'temp °C',
                'wind_speed': f"{wind_speed} м/c"
            }

        """
        response = requests.get(self.api_url, data={"lat": lat, "lon": lon},
                                headers={'X-Yandex-API-Key': self.api_key}).json()

        if (response.status_code != 200):
            return 'Error get current weather from API'

        current_weather = {'time_zone': response['info']['tzinfo']['name'],
                   'current_time': datetime.fromtimestamp(int(response['now'])).strftime('%Y-%m-%d %H:%M:%S'),
                   'condition': response['fact']['condition'],
                   'temp': response['fact']['temp'],
                   'wind_speed': response['fact']['wind_speed']
                }
        return current_weather


    def get_forecast(self, lat, lon):

        """
            TODO: return a forecast for 7 days
            [{
                    'day': i,
                    'temp': sum(temps) / len(temps),  # температуры по частям дня
                    'condition': most popular condition,  # самое популярное состояние по частям дня
                    'sunrise': sunrise,
                    'sunset': sunset
            }...]
        """
        response = requests.get(self.api_url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.api_key})

        if response.status_code != 200:
            return 'Error get current weather from API'

        day_parts = ['night', 'morning', 'day', 'evening']
        return [{'day': ind,
                     'temp': sum([day['parts'][p]['temp_avg'] for p in day_parts]) / 4,
                     'condition': Counter([day['parts'][p]['condition'] for p in day_parts]).most_common(1)[0][0],
                     'sunrise': day['sunrise'],
                     'sunset': day['sunset'],
                     }
                    for ind, day in enumerate(response['forecasts'])]


