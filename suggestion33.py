# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
慎用变长参数
'''
'''
Python支持可变长度的参数列表，可以通过在函数定义的时候使用*args和**kwargs这两种特殊的语法来是想
'''

# 补充
"""
慎用可变长度参数：
1、使用过于灵活
2、如果一个函数的参数列表很长，虽然可以使用*args和**kwargs来简化函数的定义，但通常意味着这个函数可以有更好的实现方式，应该被重构。
3、可变参数适合在下列情况下使用（不仅限于以下场景）：
A、装饰器
B、配置文件
C、子类调用父类的某些方法的时候
"""
from configparser import ConfigParser
conf = ConfigParser()
conf.read('test.cfg')
conf_dict = dict(conf.items('Default'))

name, version, platform = (None, None, None)


def func(**kwargs):
    kwargs.update(conf_dict)
    global name
    name = kwargs.get('name')
    global version
    version = kwargs.get('version')
    global platform
    platform = kwargs.get('platform')


func()
print(name, version, platform)
