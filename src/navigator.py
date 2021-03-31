#!/usr/bin/env python3

from csv import reader as csvReader


class Navigator:
    def __init__(self):
        self.subject = None
        self.code = None
        self.method = None
        self.add = False

    def navigate(self):
        subj = self.subject
        mthd = self.method
        code = self.code
        fname = f'db/{subj}/{code}-{mthd}.csv'
        with open(fname, 'r') as fd:
            self.reader = csvReader(fd)
            res = self.parse_file()
        return res

    def get_message(self, msg):
        if msg.is_subject():
            self.nullify(subj=True, code=True, mthd=True)
            self.subject = msg.get_subject()
        elif msg.is_code(self.subject):
            self.nullify(code=True, mthd=True)
            self.code = msg.get_code(self.subject)
        elif msg.is_method():
            self.nullify(mthd=True)
            self.method = msg.get_method()
        else:
            pass

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
            res += '\n\n'
        return res

    def nullify(self, subj=False, code=False, mthd=False):
        if subj or not code and not mthd:
            self.subject = None
        if code or not subj and not mthd:
            self.code = None
        if mthd or not subj and not mthd:
            self.method = None

    def parse_article(self, row):
        name, url = row
        res = f'{name}:\n{url}'
        return res

    def parse_book(self, row):
        name, author, year = row
        res = f'{name} - {author} [{year}]'
        return res

    def parse_course(self, row):
        name, platform, url = row
        res = f'{name} - {platform}:\n{url}'
        return res

    def parse_video(self, row):
        name, author, url = row
        res = f'{name} {author}:\n{url}'
        return res
