# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
很多人以为Python中不存在常量，实际上Python的内建命名空间是支持一小部分常量的。例如True,False,None
只是Python没有提供常量的直接方式而已。
那么我们可以利用以下的几种方式来进行定义。
1/通过命名风格来提醒使用者该变量代表的意义为常量，一般通用的方式是，所有的字符都是大写，然后用下划线连接各个字母。这算一种约定俗成的方式。
2/通过自定义的类实现常量功能。
'''

import const

const.COMPANY = "IBM"
try:
    const.COMPANY = "SAP"
except const.ConstError as e:
    print(e)

from constant import const
print(const.MY_SECOND_CONSTANT)
