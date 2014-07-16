# -*- coding: utf-8 -*-
__author__ = 'florije'


def readBook(book_path):
    list_books = []
    with open(book_path, 'r') as books:
        for line in books.readlines():
            line = line.strip('\n')
            tmp_books = line.split(',')
            list_books.extend([item for item in tmp_books if item != ''])
    return tuple(list_books)

import random


def dice():
    dice_num = raw_input('Please input the num of the dice_num:')
    res = {}
    for i in range(int(dice_num)):
        num = random.randint(1, 6) + random.randint(1, 6)
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
        print '%s        %s' % (i+1, num)
    for k, v in res.items():
        print '%s:%s' % (k, v*'*')

if __name__ == '__main__':
    # print readBook('books.txt')
    dice()


