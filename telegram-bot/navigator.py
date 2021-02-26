#!/usr/bin/env python3


from csv import reader as csvReader


def parse_article(row):
    name, url = row
    res = f"{name}:\n{url}\n"
    return res


def parse_book(row):
    name, author, year = row
    res = f"{name} - {author} {[year]}\n"
    return res


def parse_course(row):
    name, platform, url = row
    res = f"{name} - {platform}:\n{url}\n"
    return res


def parse_video(row):
    name, author, url = row
    res = f"{name} {author}:\n{url}\n"
    return res


def parse_file(reader, method):
    res = ""
    for row in reader:
        if method == 'a':
            res += parse_article(row)
        elif method == 'b':
            res += parse_book(row)
        elif method == 'c':
            res += parse_course(row)
        elif method == 'v':
            res += parse_video(row)
    return res


def navigate(subject, method):
    fname = '../db/' + str(subject) + '/' + str(method) + '.csv'
    with open(fname, 'r') as fd:
        reader = csvReader(fd)
        res = parse_file(reader, method)
    return res
