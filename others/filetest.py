# -*- coding: utf-8 -*-
__author__ = 'florije'
import fileinput
import datetime


def write_file():
    start_time = datetime.datetime.now()
    with open('testfile.txt', 'w') as new_file:
        # for i in xrange(1000000):
        for i in range(1000000):
            new_file.write(('%s' % i) * 200 + '\n')
    end_time = datetime.datetime.now()
    print((end_time - start_time).seconds)


def read_file():
    start_time = datetime.datetime.now()
    # with fileinput.input('testfile.txt') as f_input:
    # for line in f_input:
    #         print(line)

    f_input = fileinput.input('testfile.txt')
    for line in f_input:
        print(line)
    f_input.close()

    # with open('testfile.txt', 'r') as new_file:
    #     for line in new_file.readlines():
    #         print(line)
    end_time = datetime.datetime.now()
    print((end_time - start_time).seconds)


if __name__ == '__main__':
    # write_file()
    # read_file()

    for i in range(0, 20):
        print i
    raw_input()
    for i in range(-1, 20, 2):
        print '%d%d' % (0, 0) if i == -1 else '%d%d' % (i, i + 1)
        # if i == 0:
        #     print '%d%d' % (0, 0)
        # else:
        #     print '%d%d' % (i, i + 1)