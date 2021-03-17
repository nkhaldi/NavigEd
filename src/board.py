#!/usr/bin/env python3


from telebot.types import ReplyKeyboardMarkup as keyboard


class Board:
    def __init__(self):
        self.page = 1
        self.lcodes = list()

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
        self.lcodes = list(dcodes.keys())

        i = 0
        while i < len(self.lcodes)-1 and i < 6:
            self.codes.row(self.lcodes[i], self.lcodes[i+1])
            i += 2
        if len(self.lcodes) % 2:
            self.codes.row(self.lcodes[i])

        if len(self.lcodes) > 6:
            self.codes.row('<', '>')

    def turn_page(self, page_sign):
        if page_sign == 1:
            self.page += 1
        elif page_sign == -1:
            self.page -= 1
        else:
            pass
