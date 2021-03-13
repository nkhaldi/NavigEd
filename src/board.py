#!/usr/bin/env python3


from telebot.types import ReplyKeyboardMarkup as keyboard


class Board:
    def __init__(self):
        self.subjects = keyboard(True, True)
        self.subjects.row('Математика', 'Программирование')
        self.subjects.row('Языки', 'Прочее')
        self.subjects.row('Поддержать')

        self.methods = keyboard(True, True)
        self.methods.row('Статьи', 'Книги')
        self.methods.row('Онлайн-курсы', 'Видео')
        self.methods.row('Назад', 'Поддержать')

        self.codes = keyboard(True, True)
        self.codes.row('Основы', 'Поддержать')
