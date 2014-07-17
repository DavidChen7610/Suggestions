# -*- coding: utf-8 -*-
__author__ = 'florije'

# string = raw_input('Please input the string to encrypt:')
#
#
# def rot13(string):
#     return string.encode('rot13')
#
# print rot13(string)

string = raw_input('Please input the word:')


def get_index_char(string, *args):
    items = []
    for arg in args:
        items.append(string[arg])
    return tuple(items)

print get_index_char(string, *(0, 1, 2))