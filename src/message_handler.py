#!/usr/bin/env python3


from json import load as read_json


class Message_handler:
    def __init__(self):
        self.input = None
        self.output = None
        self.donate = 'img/donate.jpg'
        self.parse_json()

    def get_subject(self):
        if self.is_subject():
            return self.subjects[self.input]
        return False

    def is_subject(self):
        return self.input in self.subjects

    def get_code(self, subject):
        if self.is_code(subject):
            return self.codes[subject][self.input]
        return False

    def is_code(self, subject):
        return subject and self.input in self.codes[subject]

    def get_method(self):
        if self.is_method():
            return self.methods[self.input]
        return False

    def is_method(self):
        return self.input in self.methods

    def is_greeting(self):
        return self.input in self.greetings

    def greet(self, name):
        self.output = f'<b>Привет {name}!</b>\n'
        self.output += 'Что хочешь изучить?'

    def is_back(self):
        return self.input == 'назад'

    def is_help(self):
        return self.input == 'help'

    def is_thanks(self):
        return self.input in self.thanks

    def thank(self):
        self.output = f'<b>Спасибо, что вы с нами!</b>\n'
        self.output += 'Если хотите поддержать нас, '
        self.output += 'можете оформить небольшое пожертвование в BTC:'

    def parse_json(self):
        with open('json/messages.json') as msg_fd:
            msg_dict = read_json(msg_fd)
            self.greetings = msg_dict['greetings']
            self.thanks = msg_dict['thanks']
            self.subjects = msg_dict['subjects']
            self.methods = msg_dict['methods']
            self.codes = msg_dict['codes']
