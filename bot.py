import requests
import datetime
from config import TOKEN, openweather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello! Enter the your city and i'll send you info about weather")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={openweather}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_tinestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_tinestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        await message.reply(f"Weather in city: {message.text}\nTemperatur: {cur_weather}\n"
            f"Давление: {pressure} мм.рт.ст\nВетер: {wind}\n"
            f"Восход солнца: {sunrise_tinestamp}\n"
            f"Закат солнца: {sunset_tinestamp}\n"
            f"Have a nice day!"
            )

    except:
        await message.reply('City is not defined')


if __name__ == '__main__':
    executor.start_polling(dp)