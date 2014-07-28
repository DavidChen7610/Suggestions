# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
俗话说的编程其实就是处理两件事，一个事情就是处理数据，另一个就是处理字符串，对于我来说，商业应用层面的编程其实处理字符串居多，所以
掌握字符串的编程处理是一个很重要的问题，通过Python教程，读者已经掌握了基本的字符串+
'''


'''
Within a file called generators1.py, write a generator, generateMultiples(number, start) that can be configured to
generate multiples of number beginning with, and including, start. Instantiate this generator and use it to print
multiples of 3, starting with 27, up to, but not including 81.
'''


def generate_multiples(number, start):
    index = 0
    res_num = 0
    while res_num < 100:
        res_num = start + number * index
        if res_num != 81:
            yield res_num
            index += 1
        else:
            yield res_num + number
            index += 2


s = generate_multiples(3, 27)
print s

for i in s:
    print i