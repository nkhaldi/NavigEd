#!/usr/bin/env python3

from csv import reader as csvReader


def navigate(subject, method):
    fName = '../db/' + subject + '/' + method + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        key = 0
        for row in reader:
            key = printSource(row, key)


name_dict = {
    # ai
    'AI': 'ai',
    'Искуственный интеллект': 'ai',
    'ИИ': 'ai',

    # ds
    'Data Science': 'ds',
    'ds' : 'ds',

    # english
    'Английский': 'english',
    'English': 'english',

    # math
    'Математика': 'math',

    # prog
    'Программирование': 'prog'
}


def get_subject(msg):
    if msg in name_dict:
        return name_dict[msg]
    else:
        return 0
