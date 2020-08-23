#!/usr/bin/env python3

from subject import *


if __name__ == '__main__':
    subjects = {
            '1': 'Math',
            '2': 'Programming',
            '3': 'English',
            '4': 'Data Science',
            '5': 'AI'
    }

    printMenu(subjects)
    subj = readSubj(subjects)
    print(subj, '-', subjects[subj])
