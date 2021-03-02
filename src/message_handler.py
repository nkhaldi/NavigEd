#!/usr/bin/env python3


greetings = [
    "hello", "hi", "привет", "здравствуйте",
    "здравствуй", "здравствуй", "салам", "шалом"
]

thanks = [
    "thank you", "thanks", "ty", "спасибо", "спс", "поддержать"
]

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


class Message_handler:
    def __init__(self):
        self.input = ''
        self.output = ''

    def is_valid(self):
        return self.is_subject() or self.is_method()

    def get_subject(self):
        for subj in subjects:
            if self.input in subjects[subj]:
                return subj
        return False

    def get_method(self):
        for mthd in methods:
            if self.input in methods[mthd]:
                return mthd
        return False

    def is_greeting(self):
        return self.input in greetings

    def is_thanks(self):
        return self.input in thanks
