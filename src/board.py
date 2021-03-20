#!/usr/bin/env python3


from json import load as read_json
from telebot.types import ReplyKeyboardMarkup as keyboard


class Board:
    def __init__(self):
        self.brd_dict = None
        self.build_subject_board()
        self.build_method_board()

    def build_subject_board(self):
        with open('json/subjects.json') as msg_fd:
            self.brd_dict = read_json(msg_fd)
            subj_list = self.brd_dict['subjects']

        self.subjects = keyboard(True, True)
        i = 0
        while i < len(subj_list)-1 and i < 6:
            self.subjects.row(subj_list[i], subj_list[i+1])
            i += 2
        if len(subj_list) % 2:
            self.subjects.row(subj_list[i])
        self.subjects.row('Поддержать')

    def build_method_board(self):
        self.methods = keyboard(True, True)
        self.methods.row('Статьи', 'Книги')
        self.methods.row('Онлайн-курсы', 'Видео')
        self.methods.row('Назад', 'Поддержать')

    def build_code_board(self, subject):
        code_list = self.brd_dict[subject]

        self.codes = keyboard(True, True)
        i = 0
        while i < len(code_list)-1:
            self.codes.row(code_list[i], code_list[i+1])
            i += 2
        if len(code_list) % 2:
            self.codes.row(code_list[i])
