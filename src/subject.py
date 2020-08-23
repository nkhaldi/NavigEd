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

def readFromBase(subj):
    fName = '../database/' + (subjDict[subj].lower()).replace(' ', '') + '.csv'
    with open(fName, 'r') as fd:
        reader = csvReader(fd)
        for row in reader:
            for col in row:
                print(col, end='\t')
            print()
