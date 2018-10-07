# coding: utf-8
"""
建议46：使用traceback获取栈信息
"""

import traceback


gList = ['a', 'b', 'c', 'd']


def f():
    print(gList[7])


def g():
    return f()


if __name__ == '__main__':
    try:
        g()
    except IndexError as e:
        print('Sorry, Exception occured, you accessed an element out of range')
        print(e)
        traceback.print_exc()
