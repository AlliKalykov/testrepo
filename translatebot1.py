import json
import telebot

from telebot import types

from googletrans import Translator

from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    follow = types.KeyboardButton(text='/follow')
    unfollow = types.KeyboardButton(text='/unfollow')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(follow)
    markup.add(unfollow)
    bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=markup)


@bot.message_handler(commands=['follow'])
def follow(message):

    bot.send_message(message.chat.id, 'Вы подписались')


@bot.message_handler(commands=['unfollow'])
def unfollow(message):

    bot.send_message(message.chat.id, 'Вы отписались')


@bot.message_handler()
def traclate_text(message):
    if message.chat.type == 'private':
        translator = Translator()
        text = message.text
        result = translator.translate(text, dest='ru')
        bot.reply_to(message, text=result.text)
    else:
        bot.reply_to(message, text=message.text)


@bot.message_handler(content_types='photo')
def photo(message):
    print(json.dumps(message.json, indent=2))
    photo = message.photo

    photo_url = photo[-1].file_id
    bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(content_types='document')
def photo(message):
    bot.reply_to(message, 'This is document')


if '__name__' == '__main__':
    # 
    bot.infinity_polling()

