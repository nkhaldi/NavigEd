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
subject_board.row('Английский', 'Математика')
subject_board.row('Философия', 'Программирование')
subject_board.row('Поддержать')

method_board = telebot.types.ReplyKeyboardMarkup(True, True)
method_board.row('Статьи', 'Книги')
method_board.row('Онлайн-курсы', 'Видео-курсы')
method_board.row('Поддержать')

# Subject-Method dict
sm_dict = {
        's': '',
        'm': ''
}

thank_msg = f"<b>Спасибо, что вы с нами!</b>\n"
thank_msg += "Если хотите поддержать нас, "
thank_msg += "можете оформить небольшое пожертвование:"


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

    if is_thanks(msg_in):
        bot.send_message(
            message.chat.id,
            thank_msg,
            parse_mode='html',
            reply_markup=subject_board
        )
        with open('../../donate.png', 'rb') as donate:
            bot.send_photo(message.chat.id, donate)
        return

    temp = get_subject(msg_in)
    if temp:
        sm_dict['s'] = temp
        sm_dict['m'] = ''
    else:
        sm_dict['m'] = get_method(msg_in)

    if sm_dict['s'] and sm_dict['m']:
        msg_out = navigate(sm_dict['s'], sm_dict['m'])
        bot.send_message(
            message.chat.id,
            msg_out,
            parse_mode='html',
            reply_markup=subject_board
        )
    elif sm_dict['s']:
        msg_out = f"<b>Как ты хочешь изучать {msg_in}?</b>\n"
        msg_out += "- Статьи\n"
        msg_out += "- Книги\n"
        msg_out += "- Онлайн-курсы\n"
        msg_out += "- Видео\n"
        bot.send_message(
            message.chat.id,
            msg_out, parse_mode='html',
            reply_markup=method_board
        )
        return
    else:
        msg_out = f"Я пока этого не знаю."
        bot.send_message(
            message.chat.id,
            msg_out,
            parse_mode='html',
            reply_markup=subject_board
        )
        return


bot.polling(none_stop=True)
