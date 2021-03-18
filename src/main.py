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
    msg.greet(message.from_user.first_name)
    bot.send_message(
        message.chat.id,
        msg.output,
        parse_mode='html',
        reply_markup=brd.subjects
    )
    nvg.nullify(a=True)
    brd.nullify()


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
    with open('img/donate.png', 'rb') as donate:
        bot.send_photo(message.chat.id, donate)
    nvg.nullify(a=True)
    brd.nullify()


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
        nvg.nullify(a=True)
        brd.nullify()
        msg.output = 'Что ты хочешь изучить?'
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.subjects
        )
        return

    if msg.is_arrow():
        brd.turn_page(msg.page_sign)

    nvg.get_message(msg)

    if nvg.subject and nvg.code and nvg.method:
        msg.output = nvg.navigate()
        bot.send_message(
            message.chat.id,
            msg.output,
            parse_mode='html',
            reply_markup=brd.methods
        )
        nvg.nullify(m=True)
        brd.nullify()
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
        brd.build_code_board(msg.codes[nvg.subject])
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
        nvg.nullify(a=True)
        brd.nullify()


bot.polling(none_stop=True)
