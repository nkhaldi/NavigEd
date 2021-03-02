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

thank_msg = f"<b>Спасибо, что вы с нами!</b>\n"
thank_msg += "Если хотите поддержать нас, "
thank_msg += "можете оформить небольшое пожертвование:"

subject_board = get_subject_board()
method_board = get_method_board()


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    greeting = f"<b>Привет {message.from_user.first_name}!</b>\n"
    msg.output = greeting + "Что хочешь изучить?"
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
        bot.send_message(
            message.chat.id,
            thank_msg,
            parse_mode='html',
            reply_markup=subject_board
        )
        with open('../img/donate.png', 'rb') as donate:
            bot.send_photo(message.chat.id, donate)
        return

    temp = msg.get_subject()
    if temp:
        nvg.sm_dict['s'] = temp
        nvg.sm_dict['m'] = ''
    else:
        nvg.sm_dict['m'] = msg.get_method()

    if nvg.sm_dict['s'] and nvg.sm_dict['m']:
        msg.output = nvg.navigate()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=subject_board
        )
        nvg.sm_dict['m'] = 0
    elif nvg.sm_dict['s']:
        msg.output = "Как ты хочешь это изучать?"
        bot.send_message(
            message.chat.id,
            msg.output, parse_mode='html',
            reply_markup=method_board
        )
        return
    else:
        msg.output = f"Я пока этого не знаю."
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=subject_board
        )
        return


bot.polling(none_stop=True)
