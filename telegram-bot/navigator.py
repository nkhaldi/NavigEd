#!/usr/bin/env python3


from csv import reader as csvReader


def navigate(subject, method):
    fName = '../db/' + subject + '/' + method + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        res = ""
        for row in reader:
            res += f"{row}"
    return res


subj_codes = {
    # ai
    'ai': 'ai',
    'ии': 'ai',
    'искуственный интеллект': 'ai',

    # ds
    'ds': 'ds',
    'data science': 'ds',

    # eng
    'eng': 'eng',
    'english': 'eng',
    'английский': 'eng',

    # math
    'math': 'math',
    'матан': 'math',
    'математика': 'math',

    # prog
    'prog': 'prog',
    'coding': 'prog',
    'programming': 'prog',
    'программирование': 'prog'
}


def get_subject(msg):
    if msg in subj_codes:
        return subj_codes[msg]
    else:
        return False
