# coding: utf-8
"""
建议29：区别对待可变对象和不可变对象

可变对象：
字典，列表，字节数组

不可变对象：
数字，字符串，元组，None，True/False
"""


# 函数的默认参数必须是不可变对象，因为函数的一旦初始化后，默认参数便有了值，下次再调用仍是那个值
def foo(name=None):
    print(name)


def foo2(name, bag=[]):
    bag.append(name)
    print(bag)


foo2('Tom')
# ['Tom']
foo2('Jerry')
# ['Tom', 'Jerry']
