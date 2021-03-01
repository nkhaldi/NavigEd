#!/usr/bin/env python3


import telebot


# Subject menu
subject_board = telebot.types.ReplyKeyboardMarkup(True, True)
subject_board.row('ИИ', 'Data Science')
subject_board.row('Английский', 'Математика')
subject_board.row('Философия', 'Программирование')
subject_board.row('Поддержать')

# Method menu
method_board = telebot.types.ReplyKeyboardMarkup(True, True)
method_board.row('Статьи', 'Книги')
method_board.row('Онлайн-курсы', 'Видео-курсы')
method_board.row('Поддержать')
