# -*- coding: utf-8 -*-
# from collections import namedtuple
import collections

__author__ = 'florije'

'''
理解枚举替代实现的缺陷
'''


class Seasons:
    '''
    使用类属性
    '''
    Spring = 0
    Summer = 1
    Autumn = 2
    Winter = 3

print Seasons.Spring


def enum(*posarg, **keyargs):
    '''
    借助函数的方法
    :param posarg:
    :param keyargs:
    :return:
    '''
    return type("Enum", (object, ), dict(zip(posarg, xrange(len(posarg))), **keyargs))

Seasons = enum("Spring", "Summer", "Autumn", Winter=1)
print Seasons.Spring

# 使用collection.namedtuple
Seasons = collections.namedtuple('Seasons', 'Spring Summer Autumn Winter')._make(range(4))

print Seasons.Spring

'''
其实还有很多的方式，既然有这么多的实现方式，为什么人们还要坚持提出各自的建议要求语言来实现枚举呢？
其实在这些实现方式里面是有很多的不合理的层面
1、允许枚举值重复
2/支持无意义操作
'''
Seasons._replace(Spring=2)
print Seasons.Spring