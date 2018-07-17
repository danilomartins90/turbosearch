#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from ..util.color import Color

class Logger(object):
    ''' Helper object for easily printing colored text to the terminal. '''

    out_file = ''

    @staticmethod
    def pl(text):
        '''Prints text using colored format with trailing new line.'''
        Color.pl(text)

        if Logger.out_file != '':
            try:
                with open(Logger.out_file, "a") as text_file:
                    text_file.write(Color.sc(text) + '\n')
            except:
                pass