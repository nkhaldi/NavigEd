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
    final_message = greeting + "Что хочешь изучить?"
    send_mess = final_message
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message = message.text.strip().lower()
#    subject = get_subject(get_message)
    subject = get_message
    final_message = f"Ты выбрал <b>{subject}</b>."
    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
