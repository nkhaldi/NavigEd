#!/usr/bin/env python3


from json import load as read_json
from telebot.types import ReplyKeyboardMarkup as keyboard


class Board:
    def __init__(self):
        self.page = 0
        self.page_sign = None

        self.lcodes = None
        self.lsubj = None

        self.build_subject_board()
        self.build_method_board()

    def build_subject_board(self):
        self.subjects = keyboard(True, True)

        with open('json/messages.json') as msg_fd:
            msg_dict = read_json(msg_fd)
            self.lsubj = list(msg_dict['subjects'].keys())

        i = 0
        while i < len(self.lsubj)-1 and i < 6:
            self.subjects.row(self.lsubj[i], self.lsubj[i+1])
            i += 2
        if len(self.lsubj) % 2:
            self.subjects.row(self.lsubj[i])
        self.subjects.row('Поддержать')

    def build_method_board(self):
        self.methods = keyboard(True, True)
        self.methods.row('Статьи', 'Книги')
        self.methods.row('Онлайн-курсы', 'Видео')
        self.methods.row('Назад', 'Поддержать')

    def build_code_board(self, code_lst):
        self.codes = keyboard(True, True)
        self.lcodes = code_lst

        i = self.page * 6
        while i < len(self.lcodes)-1 and i < 6:
            self.codes.row(self.lcodes[i], self.lcodes[i+1])
            i += 2
        if len(self.lcodes) % 2:
            self.codes.row(self.lcodes[i])

        if len(self.lcodes) > 6:
            self.codes.row('<', '>')

    def turn_page(self, psign):
        if psign == 1:
            self.page += 1
        elif psign == -1:
            self.page -= 1
        else:
            pass

    def nullify(self):
        self.page = 0
        self.page_sign = None
        self.lcodes = None
