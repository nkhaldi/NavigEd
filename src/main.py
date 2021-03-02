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
    nvg.ms_in = message.text.strip().lower()

    if is_greeting(nvg.ms_in):
        return start(message)

    if is_thanks(nvg.ms_in):
        bot.send_message(
            message.chat.id,
            thank_msg,
            parse_mode='html',
            reply_markup=subject_board
        )
        with open('../img/donate.png', 'rb') as donate:
            bot.send_photo(message.chat.id, donate)
        return

    temp = get_subject(nvg.ms_in)
    if temp:
        nvg.sm_dict['s'] = temp
        nvg.sm_dict['m'] = ''
    else:
        nvg.sm_dict['m'] = get_method(nvg.ms_in)

    if nvg.sm_dict['s'] and nvg.sm_dict['m']:
        msg_out = navigate(nvg.sm_dict['s'], nvg.sm_dict['m'])
        bot.send_message(
            message.chat.id,
            msg_out,
            parse_mode='html',
            reply_markup=subject_board
        )
        nvg.sm_dict['m'] = 0
    elif nvg.sm_dict['s']:
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
