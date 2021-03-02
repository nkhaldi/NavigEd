#!/usr/bin/env python3


from csv import reader as csvReader


def parse_article(row):
    name, url = row
    res = f"{name}:\n{url}\n"
    return res


def parse_book(row):
    name, author, year = row
    res = f"{name} - {author} [{year}]\n"
    return res


def parse_course(row):
    name, platform, url = row
    res = f"{name} - {platform}:\n{url}\n"
    return res


def parse_video(row):
    name, author, url = row
    res = f"{name} {author}:\n{url}\n"
    return res


class Navigator:
    def __init__(self):
        msg_in = ''
        msg_out = ''
        self.sm_dict = {'s': 0, 'm': 0}


    def parse_file(self):
        res = ""
        for row in self.reader:
            if self.sm_dict['m'] == 'a':
                res += parse_article(row)
            elif self.sm_dict['m'] == 'b':
                res += parse_book(row)
            elif self.sm_dict['m'] == 'c':
                res += parse_course(row)
            elif self.sm_dict['m'] == 'v':
                res += parse_video(row)
        return res


    def navigate(self):
        subj = self.sm_dict['s']
        mthd = self.sm_dict['m']
        fname = f'../db/{subj}/{mthd}.csv'
        with open(fname, 'r') as fd:
            self.reader = csvReader(fd)
            res = self.parse_file()
        return res
