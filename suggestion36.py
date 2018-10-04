# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
俗话说的编程其实就是处理两件事，一个事情就是处理数据，另一个就是处理字符串，对于我来说，商业应用层面的编程其实处理字符串居多，所以
掌握字符串的编程处理是一个很重要的问题，通过Python教程，读者已经掌握了基本的字符串+
'''


# 补充
"""
python遇到未闭合的小括号时会自动将多行代码拼接为一行和把相邻的两个字符串字面量拼接在一起的特性，如下：
"""
s = ('SELECT * '
'FROM atable '
'WHERE afield="value"')

print(s)
# SELECT * FROM atable WHERE afield="value"


# split()和split('')采用不同的算法
# split()先去除字符串两端的空白端，然后以任意长度的空白符串作为界定符切分字符串（连续的空白符串被当作单一的空白符看待）
# split('')对于后者则认为两个连续的sep之间存在一个空字符串。
print(' a  b   c    '.split())
# ['a', 'b', 'c']
print(' a  b   c    '.split(' '))
# ['', 'a', '', 'b', '', '', 'c', '', '', '', '']
