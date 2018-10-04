#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yanghua'
'''
理解python与C语言的不同之处

1/缩进和{}
2/'与""
3/三元操作符"?:"
4/switch...case

'''


def f(num):
    return {
        0: "The first one!",  # noqa
        1: "The second one!",
        2: "The third one!"
    }.get(num, "No vainly!")


if __name__ == '__main__':
    print(f(2))
