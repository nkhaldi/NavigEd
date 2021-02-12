#!/usr/bin/env python3

from csv import reader as csvReader


def navigate(subject, method):
    fName = '../db/' + subject + '/' + method + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        key = 0
        for row in reader:
            key = printSource(row, key)


def get_subject(msg):
    if msg == "искусственный интеллект"
        return "ai"
    elif msg == "Data Sciense"
        return "ds"
    elif msg == "Английский"
        return "english"
    elif msg == "Математика":
        return "math"
    elif msg == "Программирование"
        return "prog"
    else:
        return get_msg
