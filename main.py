#!/usr/bin/env python3

from os import system as sys


def readSubj():
    print('Choose subject number >>', end=' ')
    subj = input()
    return subj


if __name__ == '__main__':
    subjects = {
            '1' : 'Math',
            '2' : 'Programming',
            '3' : 'English',
            '4' : 'Data Science',
            '5' : 'AI'
    }

    sys('clear')
    print('~~ Menu ~~')
    for subj in subjects:
        print(subj + '. ' + subjects[subj])
    while True:
        subj = readSubj()
        num = int(subj)
        if num <= len(subjects) and num > 0:
            break
    print('\nYou chose', subjects[subj])
