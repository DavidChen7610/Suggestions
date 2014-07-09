# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
Keeping the Last N Items
'''

import collections

d = collections.deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d


d1 = collections.deque()
d1.extend('abcdefg')
print 'extend    :', d1
d1.append('h')
print 'append    :', d1

d2 = collections.deque()
d2.extendleft(xrange(6))
print 'extendleft:', d2
d2.appendleft(6)
print 'appendleft:', d2

print 'From the right:'

d = collections.deque('abcdefg')
while True:
    try:
        print d.pop(),
    except IndexError:
        break
print
print 'From the left:'
d = collections.deque(xrange(6))
while True:
    try:
        print d.popleft(),
    except IndexError:
        break
print

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print pline, ','
            print line, ','  # print(line, end='')
            print('-'*20)