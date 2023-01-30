
from config import *
import requests
from pprint import pprint
import datetime



def get_weather(city, openweather):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather}&units=metric"
        )
        data = r.json()
        # pprint(data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_tinestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_tinestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f"Weather in city: {city}\nTemperatur: {cur_weather}\n"
            f"Давление: {pressure} мм.рт.ст\nВетер: {wind}\n"
            f"Восход солнца: {sunrise_tinestamp}\n"
            f"Закат солнца: {sunset_tinestamp}\n"
            f"Have a nice day!"
            )

    except Exception as ex:
        print(ex)
        print('City is not defined')

def main():
    city = input('Enter city: ')
    get_weather(city, openweather)


if __name__ == '__main__':
    main()