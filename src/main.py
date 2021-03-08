#!/usr/bin/env python3

# NavigEd telegram-bot
# @NavigEdBot
# http://t.me/NavigEdBot


import telebot

from boards import *
from navigator import *
from message_handler import *


token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)

nvg = Navigator()
msg = Message_handler()

subject_board = get_subject_board()
method_board = get_method_board()


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    msg.greet(message.from_user.first_name)
    bot.send_message(
        message.chat.id,
        msg.output,
        parse_mode='html',
        reply_markup=subject_board
    )


@bot.message_handler(content_types=['text'])
def mess(message):
    msg.input = message.text.strip().lower()

    if msg.is_greeting():
        return start(message)

    if msg.is_thanks():
        msg.thank()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=subject_board
        )
        with open('img/donate.png', 'rb') as donate:
            bot.send_photo(message.chat.id, donate)
        return

    if msg.input == 'назад':
        nvg.subject = 0
        nvg.method = 0
        msg.output = 'Что ты хочешь изучить?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=subject_board
        )
        return

    if msg.get_subject():
        nvg.subject = msg.get_subject()
        nvg.method = 0
    elif msg.get_method():
        nvg.method = msg.get_method()
    else:
        return

    if nvg.subject and nvg.method:
        msg.output = nvg.navigate()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=method_board
        )
        nvg.method = 0
    elif nvg.subject:
        msg.output = 'Как ты хочешь это изучать?'
        bot.send_message(
            message.chat.id,
            msg.output, parse_mode='html',
            reply_markup=method_board
        )
        return
    else:
        return


bot.polling(none_stop=True)
