#!/usr/bin/env python3

from main import subjDict
from os import system as sys
from csv import reader as csvReader


def printMenu(subjDict):
    sys('clear')
    print('~~ Menu ~~')
    for subj in subjDict:
        print(subj + '. ' + subjDict[subj])
    print()


def readSubj(subjDict):
    while True:
        print('Choose subject number >>', end=' ')
        subj = input()
        try:
            num = int(subj)
            if num < 1 or num > len(subjDict):
                raise ValueError
            break
        except ValueError:
            print('Invalid value!')
    return subj


def printSource(row, key):
    if row[0] is 'a' and key != 'a':
        print('\nArticles:')
        print('%-20s' % 'Name:', end='')
        print('%-20s' % 'URL:')
    elif row[0] is 'b' and key != 'b':
        print('\nBooks:')
        print('%-20s' % 'Name:', end='')
        print('%-20s' % 'Author:', end='')
        print('%-20s' % 'Year:')
    elif row[0] is 'c' and key != 'c':
        print('\nCourses:')
        print('%-20s' % 'Name:', end='')
        print('%-20s' % 'URL:')
    elif row[0] is 'v' and key != 'v':
        print('\nVideos:')
        print('%-20s' % 'Name:', end='')
        print('%-20s' % 'URL:')
    key = row[0]
    for i in range(1, len(row)):
        print('%-20s' % row[i], end='')
    print()
    return key


def readFromBase(subj):
    fName = '../database/' + (subjDict[subj].lower()).replace(' ', '') + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        key = 0
        for row in reader:
            key = printSource(row, key)
