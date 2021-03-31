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


@bot.message_handler(commands=['start'])
def start(message):
    nvg.nullify()
    msg.greet(message.from_user.first_name)
    bot.send_message(
        message.chat.id,
        msg.output,
        parse_mode='html',
        reply_markup=brd.subjects
    )


# TODO
@bot.message_handler(commands=['help'])
def help(message):
    start(message)


@bot.message_handler(commands=['support'])
def support(message):
    msg.thank()
    bot.send_message(
        message.chat.id,
        msg.output,
        parse_mode='html',
        reply_markup=brd.subjects
    )
    with open(msg.donate, 'rb') as dfd:
        bot.send_photo(message.chat.id, dfd)
    nvg.nullify()


@bot.message_handler(commands=['add'])
def add(message):
    msg.output = 'add new'
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

    if msg.is_help():
        return help(message)

    if msg.is_thanks():
        return support(message)

    if msg.is_back():
        start(message)
        nvg.nullify()
        msg.output = 'Что ты хочешь изучить?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.subjects
        )
        return

    nvg.get_message(msg)
    if nvg.subject and nvg.code and nvg.method:
        msg.output = nvg.navigate()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.methods
        )
        nvg.nullify(mthd=True)
    elif nvg.subject and nvg.code:
        msg.output = 'Как ты хочешь это изучать?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.methods
        )
    elif nvg.subject:
        msg.output = 'Какой раздел ты хочешь изучить?'
        brd.build_code_board(nvg.subject)
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.codes
        )
    else:
        msg.output = 'Что?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.subjects
        )
        nvg.nullify()


bot.polling(none_stop=True)
