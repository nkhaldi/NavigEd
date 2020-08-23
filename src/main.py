#!/usr/bin/env python3

from subject import *


subjDict = {
        '1': 'Math',
        '2': 'Programming',
        '3': 'English',
        '4': 'Data Science',
        '5': 'AI'
}


if __name__ == '__main__':

    printMenu(subjDict)
    subj = readSubj(subjDict)
    print(subj, '-', subjDict[subj])
    readFromBase(subj)
