#!/usr/bin/env python3

from csv import reader as csvReader


class Navigator:
    def __init__(self):
        self.subject = None
        self.code = None
        self.method = None

    def navigate(self):
        subj = self.subject
        mthd = self.method
        code = self.code
        fname = f'db/{subj}/{code}-{mthd}.csv'
        with open(fname, 'r') as fd:
            self.reader = csvReader(fd)
            res = self.parse_file()
        return res

    def get_subject(self, msg):
        if msg.is_subject():
            self.subject = msg.get_subject()

    # TODO
    def get_code(self, msg):
        if msg.input and self.subject:
            self.code = self.subject[0] + '01'

    def get_method(self, msg):
        if msg.is_method():
            self.method = msg.get_method()

    def parse_file(self):
        res = ''
        for row in self.reader:
            if self.method == 'a':
                res += self.parse_article(row)
            elif self.method == 'b':
                res += self.parse_book(row)
            elif self.method == 'c':
                res += self.parse_course(row)
            elif self.method == 'v':
                res += self.parse_video(row)
        return res

    def parse_article(self, row):
        name, url = row
        res = f'{name}:\n{url}\n'
        return res

    def parse_book(self, row):
        name, author, year = row
        res = f'{name} - {author} [{year}]\n'
        return res

    def parse_course(self, row):
        name, platform, url = row
        res = f'{name} - {platform}:\n{url}\n'
        return res

    def parse_video(self, row):
        name, author, url = row
        res = f'{name} {author}:\n{url}\n'
        return res
