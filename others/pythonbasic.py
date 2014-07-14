# -*- coding: utf-8 -*-
__author__ = 'florije'
import glob
import sys

flist = glob.glob('*.py')
for item in flist:
    # print(item, end=', ')
    tmp_item = item,
    print item,

sys.stdout.write("Hello World")
sys.stdout.flush()
sys.stdout.write("one line!")
sys.stdout.flush()

x = 0
y = 10


def incr(x):
    # global y
    # print y
    y = x + 1
    return y


print incr(5)
print x, y

t = ''


# def f():
# t = '1'
#
# def g():
#         t += '2'
#         return t
#
#     return g
#
#
# print f()()


def d():
    global t
    t = 2

    def g():
        global t
        t += 1
        return t

    return g


print d()()


def a():
    x = 0

    def b():
        print locals()
        y = x + 1
        print locals()
        print x, y

    return b


a()()


# def a():
#     x = 0
#
#     def b():
#         nonlocal x
#         x += 1
#         print x
#
#     return b
#
#
# a()()

print [n for n in xrange(11) if not bool(n % 2)]


def create_multipliers():
    return [lambda x: i * x for i in range(5)]

cr = create_multipliers()

for multiplier in create_multipliers():
    print(multiplier(2))
