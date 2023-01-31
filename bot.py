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
    await message.reply("Привет! Отправь мне название города")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={openweather}&units=metric"
        )
        data = r.json()
        city = data["name"]
        temp = data["main"]["temp"]
        feelike = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        visibility = data["visibility"]
        wind = data["wind"]["speed"]

        await message.reply(f"Погода по городу {city.title()}:\nТемпература: {temp}°C, но чувствуется как {feelike}°C\nДавление: {pressure}, влажность: {humidity}\nВидимость: {visibility} метров\nСкорость ветра {wind}м/c")
    except:
        await message.reply('City is not defined')

if __name__ == '__main__':
    executor.start_polling(dp)
    

