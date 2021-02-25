#!/usr/bin/env python3

# NavigEd telegram-bot
# @NavigEdBot
# http://t.me/NavigEdBot


import telebot

from navigator import *
from message_handler import *


token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)

subject_board = telebot.types.ReplyKeyboardMarkup(True, True)
subject_board.row('ИИ', 'Data Science')
subject_board.row('Английский', 'Математка')
subject_board.row('Программирование', 'Философия')

ms = {
        's': '',
        'm': ''
}


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    greeting = f"<b>Привет {message.from_user.first_name}!</b>\n"
    msg_out = greeting + "Что хочешь изучить?"
    bot.send_message(
        message.chat.id,
        msg_out,
        parse_mode='html',
        reply_markup=subject_board
    )


@bot.message_handler(content_types=['text'])
def mess(message):
    msg_in = message.text.strip().lower()

    if is_greeting(msg_in):
        return start(message)

    subject = get_subject(msg_in)
    method = get_method(msg_in)

    if subject and method:
        ms['m'] = method
        msg_out = navigate(ms['s'], ms['m'])
    elif subject:
        ms['s'] = subject
        msg_out = f"<b>Как ты хочешь изучать {msg_in}?</b>\n"
        msg_out += "- Статьи\n"
        msg_out += "- Книги\n"
        msg_out += "- Интерактивные курсы\n"
        msg_out += "- Видео\n"
    else:
        msg_out = f"Я пока этого не знаю."
        bot.send_message(
            message.chat.id,
            msg_out,
            parse_mode='html',
            reply_markup=subject_board
        )
        return

    bot.send_message(
        message.chat.id,
        msg_out, parse_mode='html',
        reply_markup=subject_board
    )


bot.polling(none_stop=True)
