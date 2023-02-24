import requests
import datetime
from config import TOKEN, API
import telebot
# from aiogram import Bot, types
from telebot import types
import aiogram


bot = telebot.TeleBot(token=TOKEN)

# dp = Dispatcher(bot)

@bot.message_handler(commands=["start"])
def start_commands(message):
    # start = types.KeyboardButton(text='/start')
    bish = types.KeyboardButton(text='/Bishkek')
    almaty = types.KeyboardButton(text='/Almaty')
    tashkent = types.KeyboardButton(text='/Tashkent')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(bish, almaty, tashkent)
    
    bot.send_message(message.chat.id, "Добро пожаловать!\nВыберите город для сводки погоды.", reply_markup=markup)

@bot.message_handler(commands=["Bishkek"])
def get_weather_bishkek(message):
    # bish = types.KeyboardButton(text='/Bishkek')
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # markup.add(bish)
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "rain": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B" 
    }

    lat = '42.87'
    lon = '74.59'
    r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"
        )
    data = r.json()

    city = data["name"]
    cur_weather = data["main"]["temp"]

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "Посмотри в окно, я не могу понять что за погода!"

    humidity = data["main"]["humidity"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\nВлажность: {humidity}%\n"
          f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")


@bot.message_handler(commands=["Almaty"])
def get_weather_almaty(message):
    
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "rain": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B" 
    }

    lat = '43.2567'
    lon = '76.9286'
    r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"
        )
    data = r.json()

    city = data["name"]
    cur_weather = data["main"]["temp"]

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "Посмотри в окно, я не могу понять что за погода!"

    humidity = data["main"]["humidity"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\nВлажность: {humidity}%\n"
          f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")


@bot.message_handler(commands=["Tashkent"])
def get_weather_tashkent(message):
    
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "rain": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B" 
    }

    lat = '41.2646'
    lon = '69.2163'
    r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric"
        )
    data = r.json()

    city = data["name"]
    cur_weather = data["main"]["temp"]

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "Посмотри в окно, я не могу понять что за погода!"

    humidity = data["main"]["humidity"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
        f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\nВлажность: {humidity}%\n"
          f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")


@bot.message_handler(content_types=['text', 'voice', 'document', 'photo'])
def ans_text(message):
    bot.send_message(message.chat.id, 'Используйте только команды')

# def regiater_hendlers():
#     bot.register_message_handler(start_commands)
#     bot.register_message_handler(fdkn)

if __name__ == '__main__':
    bot.infinity_polling()
