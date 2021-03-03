#!/usr/bin/env python3


import telebot


# Subjects menu
def get_subject_board():
    subject_board = telebot.types.ReplyKeyboardMarkup(True, True)
    subject_board.row('Искуственный интеллект', 'Data Science')
    subject_board.row('Английский', 'Математика')
    subject_board.row('Философия', 'Программирование')
    subject_board.row('Поддержать')
    return subject_board


# Methods menu
def get_method_board():
    method_board = telebot.types.ReplyKeyboardMarkup(True, True)
    method_board.row('Статьи', 'Книги')
    method_board.row('Онлайн-курсы', 'Видео-курсы')
    method_board.row('Назад', 'Поддержать')
    return method_board
