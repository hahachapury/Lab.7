import requests
print('task 1 ------------------------------------------------------------')

API_1 = 'a3191f57fc23df8b3796e12eee1a3073'
LAT = 68.98
LON = 33.09

def get_weather():
    Weather_URL = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': LAT,
        'lon': LON,
        'appid': API_1,
        'lang': 'ru'
    }
    response = requests.get(Weather_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print(f'Failed to get weather data for {response.status_code}')

city_info = get_weather()
if city_info:
    print(f' Город - {city_info['name']}', "\n",
          f'Погода - {city_info["weather"][0]["description"]}', "\n",
          f'Влажность - {city_info["main"]["humidity"]} %', "\n",
          f'Давление - {city_info["main"]["pressure"]} мм ртутного столба', "\n")


print('task2 --------------------------------------------------------------')

API_2 = '44ff1b93-9910-4535-993d-078c1d8bec48'

weekday_translation = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}

def get_holiday():
    Holiday_URL = 'https://holidayapi.com/v1/holidays'
    country = input("Выберите страну (впишите её код): ").upper()

    params = {
        'key': API_2,
        'country': country,
        'year': 2025,
        'language': 'ru',
        'pretty': 1
    }
    response = requests.get(Holiday_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print(f'Failed to get weather data for {response.status_code}')
        return None

holiday_info = get_holiday()
if holiday_info and 'holidays' in holiday_info:
    for i, holiday in enumerate(holiday_info['holidays'][:7]):
        is_public = 'Да' if holiday['public'] else 'Нет'
        weekday_en = holiday['weekday']['date']['name']
        weekday_ru = weekday_translation.get(weekday_en, weekday_en)
        print(f'{i + 1}-й праздник в 2025 году - {holiday["name"]},')
        print(f'отмечается {holiday["date"]} (гггг-мм-дд),')
        print(f'государственный - {is_public},')
        print(f'день недели - {weekday_ru}\n')
