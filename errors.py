#!/usr/bin/env python3


class SubjectNumberError(Exception):
    def __init__(self, text):
        self.txt = 'Wrong number!'
