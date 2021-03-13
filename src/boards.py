#!/usr/bin/env python3


from telebot.types import ReplyKeyboardMarkup as keyboard


# Subjects menu
def get_subject_board():
    subject_board = keyboard(True, True)
    subject_board.row('Математика', 'Программирование')
    subject_board.row('Языки', 'Прочее')
    subject_board.row('Поддержать')
    return subject_board


# Methods menu
def get_method_board():
    method_board = keyboard(True, True)
    method_board.row('Статьи', 'Книги')
    method_board.row('Онлайн-курсы', 'Видео')
    method_board.row('Назад', 'Поддержать')
    return method_board


def get_code_board(codes):
    code_board = keyboard(True, True)
    code_board.row('Основы', 'Поддержать')
    return code_board
