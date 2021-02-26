#!/usr/bin/env python3


def is_greeting(msg):
    greetings = [
        "hello", "hi", "привет", "здравствуйте",
        "здравствуй", "здравствуй", "салам", "шалом"
    ]
    return msg in greetings


def is_thanks(msg):
    thanks = [
        "thank you", "thanks", "ty", "спасибо", "спс"
    ]
    return msg in thanks


def get_subject(msg):
    for subj in subjects:
        if msg in subjects[subj]:
            return subj
    return False


def get_method(msg):
    for meth in methods:
        if msg in methods[meth]:
            return meth
    return False


subjects = {
        'ai':
        ['ai', 'ии', 'искуственный интеллект'],
        'ds':
        ['ds', 'data science'],
        'eng':
        ['eng', 'english', 'английский'],
        'math':
        ['math', 'матан', 'математика'],
        'philosofy':
        ['philosofy', 'философия'],
        'prog':
        ['prog', 'coding', 'programming', 'программирование']
}

methods = {
        'a': ['a', 'articles', 'статьи'],
        'b': ['b', 'books', 'книги'],
        'c': ['c', 'courses', 'курсы', 'онлайн-курсы'],
        'v': ['v', 'videos', 'видео', 'видеокурсы']
}
