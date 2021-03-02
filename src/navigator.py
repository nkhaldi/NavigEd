#!/usr/bin/env python3


from csv import reader as csvReader


class Navigator:
    def __init__(self):
        msg_in = ''
        msg_out = ''
        self.sm_dict = {'s': 0, 'm': 0}

    def navigate(self):
        subj = self.sm_dict['s']
        mthd = self.sm_dict['m']
        fname = f'../db/{subj}/{mthd}.csv'
        with open(fname, 'r') as fd:
            self.reader = csvReader(fd)
            res = self.parse_file()
        return res

    def parse_file(self):
        res = ""
        for row in self.reader:
            if self.sm_dict['m'] == 'a':
                res += self.parse_article(row)
            elif self.sm_dict['m'] == 'b':
                res += self.parse_book(row)
            elif self.sm_dict['m'] == 'c':
                res += self.parse_course(row)
            elif self.sm_dict['m'] == 'v':
                res += self.parse_video(row)
        return res

    def parse_article(self, row):
        name, url = row
        res = f"{name}:\n{url}\n"
        return res

    def parse_book(self, row):
        name, author, year = row
        res = f"{name} - {author} [{year}]\n"
        return res

    def parse_course(self, row):
        name, platform, url = row
        res = f"{name} - {platform}:\n{url}\n"
        return res

    def parse_video(self, row):
        name, author, url = row
        res = f"{name} {author}:\n{url}\n"
        return res
