#!/usr/bin/env python3

from os import system as sys


def printMenu(subjects):
    sys('clear')
    print('~~ Menu ~~')
    for subj in subjects:
        print(subj + '. ' + subjects[subj])
    print()


def readSubj(subjects):
    while True:
        print('Choose subject number >>', end=' ')
        subj = input()
        try:
            num = int(subj)
            if num < 1 or num > len(subjects):
                raise ValueError
            break
        except ValueError:
            print('Invalid value!')
    return subj
