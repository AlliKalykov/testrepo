import telebot
from googletrans import Translator
import csv

import json

from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])  ## ОТВЕЧАЕТ ЗА КОМАНДУ START
def start(message):
    print(message.json)
    bot.send_message(message.chat.id, "Добро пожаловать!")
    user = message.from_user
    user_info = f"Никнейм: {user.username}\nФамилия: {user.last_name}\nИмя: {user.first_name}\nId: {user.id}"

## Записываем в txt файл
    with open('user.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([user.username, user.id])

@bot.message_handler(content_types='photo')
def photo(message):
    print(json.dumps(message.json, indent=2))
    photo = message.photo

    photo_url = photo[-1].file_id
    bot.send_photo(message.chat.id, photo_url)

@bot.message_handler(content_types=['voice'])
def voice_to_text(message):
    bot.reply_to(message, 'voice')


@bot.message_handler(commands=['mycommand'])
def mycommand(message):
    with open('user.csv', 'r') as f:
        # прочитать данные с файла, взять все данные с поля id и сделать рассылку. (дополнительно обработать момент отписки, или ошибку telebot.apihelper.ApiTelegramException)
        pass 
    # bot.send_message(528857607, 'Кастомная команда')
    bot.send_message(787995209, 'Кастомная команда')
    bot.send_message(5873445472, 'Кастомная команда')
    bot.send_message(477072660, 'Кастомная команда')

@bot.message_handler()
def traclate_text(message):
    user = message.from_user.username
    if message.chat.type == 'private':
        translator = Translator()
        text = message.text 
        result = translator.translate(text, dest='ru')
        bot.reply_to(message, text=result.text)
    else:
        bot.reply_to(message, text=message.text)
    
    with open('translate_text.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow(["Исходный текст", "Переведенный текст", "Пользователь"])
        csv_file.writerow([text, result.text, user])

bot.infinity_polling()


## Каждый кто запускает бот, нужно записать в user.txt файл:
# никнейм
# фамилия
# имя
## Написать в csv файл текст который переводит бот(исходный текст, переведенный текст, пользователь)
## Напишите хэндлер (функцию), которая отвечает на картинку картинкой
## Написать функцию которая реагирует на определенную команду и отправляет всм пользователям с user.txt сообщение "Привет мир!"

12888615, 12791353, 12874330, 12931996, 12802264, 12786453, 12798372, 12923527, 12884315, 12866978, 12919340, 12798383, 12925559, 12856606, 12862888, 12839171, 12893683, 12858568, 12828165, 12825839, 12852953, 12858910, 12781902, 12909609

`'id', 'channel_id', 'message_test', 'sender', 'max_similar_stop_words', 'message_id', 'message_send_date', 'entities', 'clean_message', 'description', 'sender_username', 'channel_id_from'`