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

    def build_code_board(self, dcodes):
        self.codes = keyboard(True, True)
        lcodes = list(dcodes.keys())
        print(lcodes)
        if len(lcodes) % 2:
            i = 0
            while i < len(lcodes)-1:
                self.codes.row(lcodes[i], lcodes[i+1])
                i += 2
            self.codes.row(lcodes[i])
        else:
            for i in range(0, len(lcodes)-1, 2):
                self.codes.row(lcodes[i], lcodes[i+1])
        self.methods.row('Назад', 'Поддержать')
