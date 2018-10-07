# coding: utf-8
"""
建议36：掌握字符串的基本用法

字符串的常用函数

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
