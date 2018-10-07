# coding: utf-8
"""
建议7：将常量集中到一个文件

Python没有提供常量的直接方式，那么我们可以利用以下的几种方式来进行定义：
1，通过命名风格来提醒使用者该变量代表的意义为常量，一般通用的方式是，所有的字符都是大写，
然后用下划线连接各个字母，这算一种约定俗成的方式，缺点是对应的值仍可变。
2，通过自定义的类实现常量功能。要求符合“命名全部为大写”和“值一量绑定便不可再修改”两个条件。
自定义类放在const.py
常量集中到一个文件constant.py
"""

import const

const.COMPANY = "IBM"
try:
    const.COMPANY = "SAP"
except const.ConstError as e:
    print(e)
try:
    const.company = 'AMD'
except const.ConstError as e:
    print(e)


from constant import const  # noqa
print(const.MY_SECOND_CONSTANT)
