#!/usr/bin/env python3

# Head or Tail Telegram bot
# @Head_or_Tail_Bot
# http://t.me/Head_or_Tail_Bot


import telebot

from navigator import *
from message_handler import *


token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    greeting = f"<b>Привет {message.from_user.first_name}!</b>\n"
    msg_out = greeting + "Что хочешь изучить?"
    bot.send_message(message.chat.id, msg_out, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    msg_in = message.text.strip().lower()

    if is_greeting(msg_in):
        start(message)
        return

    subject = get_subject(msg_in)
    if subject:
        msg_out = f"Ты выбрал <b>{msg_in}</b>."
    else:
        msg_out = "Я пока этого не знаю."

    bot.send_message(message.chat.id, msg_out, parse_mode='html')

    if not subject:
        return

    msg_out = "<b>Как ты предпочитаешь учиться?</b>\n"
    msg_out += "- Статьи\n"
    msg_out += "- Книги\n"
    msg_out += "- Интерактивные курсы\n"
    msg_out += "- Видео\n"
    bot.send_message(message.chat.id, msg_out, parse_mode='html')


bot.polling(none_stop=True)
