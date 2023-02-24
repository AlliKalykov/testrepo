import requests
import datetime
import telebot
from config import TOKEN_W, API_W
from telebot import types

bot = telebot.TeleBot(token=TOKEN_W)

@bot.message_handler(commands=['start'])
def weather_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb = types.KeyboardButton(text='Homes')
    pogoda = types.KeyboardButton(text='Weather!')
    markup.row(kb, pogoda)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def weather_get(message):
    code_smile = {
        'Clear': 'Clear \U00002600',
        'Clouds': 'Clouds \U00002601',
        'Rain': 'Rain \U00002614',
        'Drizzle': 'Drizzle \U00002614',
        'Thunderstorm': 'Thunderstorm \U000026A1',
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }
    if message.text == 'Weather!':
        bot.reply_to(message, 'Enter the your CITY!')
    elif message.text == 'Homes':
        weather_start(message)
    else:
        try:
            URL = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&units=metric&appid={API_W}'
            )
            js = URL.json()
            # print(js)

            city = js['name']
            country = js['sys']['country']
            temp_city = js['main']['temp']

            weather_desp = js['weather'][0]['main']
            if weather_desp in code_smile:
                wd = code_smile[weather_desp]
            else:
                wd = "Some kind of bullshit"

            wind_city = js['wind']['speed']
            sunrise = datetime.datetime.fromtimestamp(js['sys']['sunrise'])
            sunset = datetime.datetime.fromtimestamp(js['sys']['sunset'])

            bot.reply_to(message,
                        f"Country: {country}\nWeather in city: {city}\nTemperature: {temp_city} {wd}\nWind: {wind_city}\n"
                        f"Sunrise{sunrise}\nSunset: {sunset}\n"
                        f"Have a good day!"
                        )

        except:
            bot.reply_to(message, 'Enter the correct name city!')

# @bot.message_handler()
# def answer(message):
#     if message.text == 'Weather!':
#         bot.reply_to(message, 'Enter the your CITY!')

#     elif message.text == 'Homes':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         kb = types.KeyboardButton(text='Home')
#         pogoda = types.KeyboardButton(text='Weather!')
#         markup.row(kb, pogoda)

#         bot.send_message(message.chat.id, "Home".format(message.from_user), reply_markup=markup)

if __name__ == '__main__':
    bot.infinity_polling()