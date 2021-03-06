#!/usr/bin/env python3


import json


class Message_handler:
    def __init__(self):
        self.input = 0
        self.output = 0
        self.init_json()

    def get_subject(self):
        if self.input in self.subjects:
            return self.subjects[self.input]
        return False

    def get_method(self):
        if self.input in self.methods:
            return self.methods[self.input]
        return False

    def is_greeting(self):
        return self.input in self.greetings

    def greet(self, name):
        self.output = f'<b>Привет {name}!</b>\n'
        self.output += 'Что хочешь изучить?'

    def init_json(self):
        with open('json/messages.json') as fd:
            msg_dict = json.load(fd)
            self.greetings = msg_dict['greetings']
            self.thanks = msg_dict['thanks']
            self.subjects = msg_dict['subjects']
            self.methods = msg_dict['methods']

    def is_thanks(self):
        return self.input in self.thanks

    def thank(self):
        self.output = f'<b>Спасибо, что вы с нами!</b>\n'
        self.output += 'Если хотите поддержать нас, '
        self.output += 'можете оформить небольшое пожертвование:'
