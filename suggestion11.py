# coding: utf-8
"""
建议11：理解枚举替代实现的缺陷

Python2.7后使用第三方模块flufl.enum
Python3.4后使用内置枚举Enum，它参考实现了flufl.enum
"""

# python3.5提供enum库
from enum import Enum


class Seasons(Enum):
    Spring = 'Spring'
    Summer = 2
    Autumn = 3
    Winter = 4


for member in Seasons.__members__:
    print(member)

print(Seasons.Spring.value, Seasons.Summer.value, Seasons.Autumn.value, Seasons.Winter.value)
