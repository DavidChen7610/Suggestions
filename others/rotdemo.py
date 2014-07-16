# -*- coding: utf-8 -*-
__author__ = 'florije'

string = raw_input('Please input the string to encrypt:')


def rot13(string):
    return string.encode('rot13')

print rot13(string)
