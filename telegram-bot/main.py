#!/usr/bin/env python3

# Head or Tail Telegram bot
# @Head_or_Tail_Bot
# http://t.me/Head_or_Tail_Bot


import telebot

from subjects import *

token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    greeting = f"<b>Привет {message.from_user.first_name}!</b>\n"
    fin_msg = greeting + "Что хочешь изучить?"
    bot.send_message(message.chat.id, fin_msg, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message = message.text.strip().lower()
    subject = get_subject(get_message)
    fin_msg = f"Ты выбрал <b>{subject}</b>."
    bot.send_message(message.chat.id, fin_msg, parse_mode='html')

    fin_msg = "<b>Как ты предпочитаешь учиться?</b>\n"
    fin_msg += "- Статьи\n"
    fin_msg += "- Книги\n"
    fin_msg += "- Интерактивные курсы\n"
    fin_msg += "- Видео\n"
    bot.send_message(message.chat.id, fin_msg, parse_mode='html')

    method = get_message = message.text.strip().lower()
    fin_msg = f"Ты выбрал <b>{method}</b>."
    bot.send_message(message.chat.id, fin_msg, parse_mode='html')


bot.polling(none_stop=True)
