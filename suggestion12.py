# coding: utf-8
"""
建议12：不找茬使用type来进行类型检查

作为动态性的强类型脚本语言，Python中的变量在定义的时候并不会指明具体类型，Python解释器
会在运行时自动进行类型检查并根据需要进行隐式类型转换，按照Python的里面，为了充分利用其
动态性的特性，是不推荐进行类型检查的。

使用isinstance(obj, (Type1[,Type2...]))
"""


def add(a, b):
    return a + b


print(add(1, 2))
print(add('a', 'b'))
print(add(1, 2j))
print(add(1.1, 2.3))
print(add([1, 2], [3, 4]))
# print(add(1, 'a'))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(isinstance(2, float))
print(isinstance(int, float))
print(isinstance((2, 3), (str, list, tuple)))
