# coding: utf-8
"""
建议15：使用enumerate()获取序列迭代的索引和值

函数enumerate()方法是在Python2.3中引入的，主要是为了解决在循环中获取索引以及对应的值的问题，
它具有一定的惰性，每次仅在需要的时候产生一个index,item对，其函数签名是：
enumerate(sequence, start=0)
其中sequence可以为序列，如list或者set，也可以为一个iterator或者任何可以进行迭代的对象，
默认的start为0，函数返回本质是一个迭代器，可以直接使用next方法来进行获取下一个元素。

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""

li = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(li):
    print('index:', i, 'element:', e)


# 自定义enumerate功能，实现反向显示
def myenumerate(sequence):
    n = -1
    for elem in reversed(sequence):
        yield len(sequence) + n, elem
        n -= 1


print()
for i, e in myenumerate(li):
    print('index:', i, 'element:', e)
