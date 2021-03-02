#!/usr/bin/env python3


greetings = [
    "hello", "hi", "привет", "здравствуйте",
    "здравствуй", "здравствуй", "салам", "шалом"
]

thanks = [
    "thank you", "thanks", "ty", "спасибо", "пока", "поддержать"
]


subjects = {
        'data science': 'ds',
        'английский': 'eng',
        'искуственный интеллект': 'ai',
        'математика': 'math',
        'программирование': 'prog',
        'философия': 'philosofy'
}

methods = {
        'статьи': 'a',
        'книги': 'b',
        'курсы': 'c',
        'онлайн-курсы': 'c',
        'видео': 'v',
        'видео-курсы': 'v'
}


class Message_handler:
    def __init__(self):
        self.input = 0
        self.output = 0

    def get_subject(self):
        if self.input in subjects:
            return subjects[self.input]
        return False

    def get_method(self):
        if self.input in methods:
            return methods[self.input]
        return False

    def is_greeting(self):
        return self.input in greetings

    def greet(self, name):
        self.output = f"<b>Привет {name}!</b>\n"
        self.output += "Что хочешь изучить?"


    def is_thanks(self):
        return self.input in thanks

    def thank(self):
        self.output = f"<b>Спасибо, что вы с нами!</b>\n"
        self.output += "Если хотите поддержать нас, "
        self.output += "можете оформить небольшое пожертвование:"
