#!/usr/bin/env python3


from csv import reader as csvReader


def navigate(subject, method):
    fName = '../db/' + subject + '/' + method + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        res = ""
        for row in reader:
            res += f"{row}"
    return res
