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

# Subject-Method dict
sm_dict = dict()

thank_msg = f"<b>Спасибо, что вы с нами!</b>\n"
thank_msg += "Если хотите поддержать нас, "
thank_msg += "можете оформить небольшое пожертвование:"

subject_board = get_subject_board()
method_board = get_method_board()


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
        with open('../img/donate.png', 'rb') as donate:
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
        sm_dict = dict()
    elif sm_dict['s']:
        msg_out = "Как ты хочешь это изучать?"
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
