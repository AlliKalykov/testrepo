# import json
# import telebot
# from googletrans import Translator

# from config import TOKEN

# bot = telebot.TeleBot(token=TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     # print(json.dumps(message.json, indent=2))
#     bot.send_message(message.chat.id, 'Добро пожаловать!')

# @bot.message_handler()
# def traclate_text(message):
#     if message.chat.type == 'private':
#         translator = Translator()
#         text = message.text
#         result = translator.translate(text, dest='ru')
#         bot.reply_to(message, text=result.text)
#     else:
#         bot.reply_to(message, text=message.text)

# bot.infinity_polling()
# __________________________________________________________________________________________________
# Nurislam tasks 2023-02-22 ⬇️
import json
import telebot
from googletrans import Translator

from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)

# 1. Написить в текстовый файл users.txt пользователей которые запускают 
# бота (никнейм, фамилия, имя,  id)
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    with open('users.txt', 'a') as f:
        f.write(f"{user.username}, {user.last_name}, {user.first_name}, {user.id}\n")
    bot.send_message(message.chat.id, 'Добро пожаловать!')
    print(start)

# 2. Написать в csv файл текст который переводит бот (исходный текст, переведенный текст, пользователь)
import csv

# 3. Напишите хендлер (функцию), которая отвечает на картинку картинкой
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    photo = message.photo[-1]  # берем последнюю (самую большую) фотографию из списка
    bot.send_photo(message.chat.id, photo.file_id)


# 4. Написать функцию, которая реагирует на определенную команду и отправляет всем пользователям 
# с users.txt сообщение "Привет мир!"
@bot.message_handler(commands=['hello'])
def send_hello(message):
    with open('users.txt', 'r') as f:
        for line in f:
            user = line.strip().split(', ')
            bot.send_message(user[-1], 'Привет мир!')


@bot.message_handler()
def translate_text(message):
    if message.chat.type == 'private':
        translator = Translator()
        text = message.text
        result = translator.translate(text, dest='ru')
        bot.reply_to(message, text=result.text)
        
        user = message.from_user
        with open('translations.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([text, result.text, f"{user.username}, {user.last_name}, {user.first_name}"])
    else:
        bot.reply_to(message, text=message.text)

bot.infinity_polling()