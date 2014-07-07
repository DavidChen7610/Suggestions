# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

'''
基本上所有的项目中都存在对序列进行迭代并获取序列中得元素进行处理的场景，这是一个非常普通而且简单的需求，相信很多人一口气能写出来很多的实现
'''

# 在每次循环中对索引变量进行自增
li = ['a', 'b', 'c', 'd', 'e']
index = 0
for i in li:
    print 'index:', index, 'element:', i
    index += 1

# 使用range()和len()方法结合
for i in range(len(li)):
    print 'index:', i, 'element:', li[i]

# 使用while循环，用len()获取循环次数
index = 0
while index < len(li):
    print 'index:', index, 'element:', li[index]
    index += 1

# 使用zip()方法
for i, e in zip(range(len(li)), li):
    print 'index:', i, 'element:', e

# 使用enumerate()方法获取序列迭代的索引和值
for i, e in enumerate(li):
    print 'index:', i, 'element:', e

'''
这里推荐的是使用方法五，因为它代码清晰简洁，可读性好，函数enumerate()方法是在Python2.3中引入的，主要是为了解决在循环中获取索引
以及对应的值的问题，它具有一定的惰性，每次仅在需要的时候产生一个index,item对，
其函数签名是：
enumerate(sequence, start=0)
其中sequence可以为序列，如list或者set，也可以为一个iterator或者任何可以进行迭代的对象，默认的start为0，函数返回本质是一个迭代器，
可以直接使用next方法来进行获取下一个元素
'''
e = enumerate(li)
print e
print e.next()

'''
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
'''

# 以上是函数的内部实现，其实自己可以按照类似的方式，自己尽情实现。


def myenumerate(sequence, start=0):
    n = -1
    for elem in sequence:
        yield len(sequence) + n, elem
        n -= 1

for i, e in myenumerate(li):
    print 'index:', i, 'element:', e

'''
需要注意的是，对于字典的迭代，并不适合，因为字典默认是要被转化为序列进行处理
'''
personinfo = {
    'name': 'Jon',
    'age': 20,
    'hobby': 'football'
}

for k, v in enumerate(personinfo):
    print k, v

'''
0 hobby
1 age
2 name
'''

for k, v in personinfo.iteritems():
    print k, v

'''
hobby football
age 20
name Jon
'''