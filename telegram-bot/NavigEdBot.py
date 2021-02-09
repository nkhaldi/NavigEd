#!/usr/bin/env python3

# Head or Tail Telegram bot
# @Head_or_Tail_Bot
# http://t.me/Head_or_Tail_Bot


import telebot
from random import randrange


token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    msg = f"<b>Привет {message.from_user.first_name}!</b>\nХочешь учиться?"
    send_mess = msg
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message = message.text.strip().lower()
    msg = "Я пока ничего не умею, но скоро научу тебя всему, что узнаю сам!"
    bot.send_message(message.chat.id, msg, parse_mode='html')


bot.polling(none_stop=True)
