#!/usr/bin/env python3

# NavigEd telegram-bot
# @NavigEdBot
# t.me/NavigEdBot


from telebot import TeleBot

from board import Board
from navigator import Navigator
from message_handler import Message_handler


token_file = open('/home/narek/.pass/.naviged.token')
token = token_file.read().rstrip('\n')
bot = TeleBot(token)

brd = Board()
nvg = Navigator()
msg = Message_handler()


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    msg.greet(message.from_user.first_name)
    bot.send_message(
        message.chat.id,
        msg.output,
        parse_mode='html',
        reply_markup=brd.subjects
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
            reply_markup=brd.subjects
        )
        with open('img/donate.png', 'rb') as donate:
            bot.send_photo(message.chat.id, donate)
        return

    if msg.is_back():
        nvg.subject = 0
        nvg.code = 0
        nvg.method = 0
        msg.output = 'Что ты хочешь изучить?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.subjects
        )
        return

    nvg.get_subject(msg)
    nvg.get_code(msg)
    nvg.get_method(msg)

    if nvg.subject and nvg.code and nvg.method:
        msg.output = nvg.navigate()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.methods
        )
        nvg.method = 0
    elif nvg.subject:
        msg.output = 'Как ты хочешь это изучать?'
        bot.send_message(
            message.chat.id,
            msg.output, parse_mode='html',
            reply_markup=brd.methods
        )
        return
    else:
        return


bot.polling(none_stop=True)
