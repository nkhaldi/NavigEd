#!/usr/bin/env python3


def is_greeting(msg):
    if msg == "hello" or    \
            msg == "hi" or  \
            msg == "привет":
        return True
    else:
        return False


def get_subject(msg):
    for subj in subjects:
        if msg in subjects[subj]:
            return subj
    return False


subjects = {
        'ai':   ['ai', 'ии', 'искуственный интеллект'],
        'ds':   ['ds', 'data science'],
        'eng':  ['eng', 'english', 'английский'],
        'math': ['math', 'матан', 'математика'],
        'prog': ['prog', 'coding', 'programming', 'программирование']
}
