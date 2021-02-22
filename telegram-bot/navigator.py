#!/usr/bin/env python3


from csv import reader as csvReader


def navigate(subject, method):
    fname = '../db/' + str(subject) + '/' + str(method) + '.csv'
    with open(fname, 'r') as fd:
        reader = csvReader(fd)
        res = ""
        for row in reader:
            res += f"{row}\n"
    return res
