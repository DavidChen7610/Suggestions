# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
作为动态性的强类型脚本语言，Python中的变量在定义的时候并不会指明具体类型，Python解释器会在运行时自动进行类型检查并根据需要进行隐式类型
转换，按照Python的里面，为了充分利用其动态性的特性，是不推荐进行类型检查的，
'''
def add(a, b):
    return a + b

print add(1, 2)
print add('a', 'b')
print add(1, 2j)
print(add(1.1, 2.3))
print(add([1, 2], [3, 4]))
# print(add(1, 'a'))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 不刻意进行类型检查，而是在出错的情况下通过抛出异常进行处理，这是较为常见的方式，但是实际应用中为了提高程序的健壮性，仍然会面临需要进行
# 类型检查的需求，那一般人就会直接想到type

'''
内建函数type用于返回当前对象的类型，因此可以通过与Python自带模块types中所定义的名称进行对比，根据其返回的值来确定变量类型是否符合要求
'''
import types
if type([]) is types.ListType:
    print 'Yeap! you are a list!'
# 所有基本类型对应的名称都可以在types模块中找到，然而使用type函数并不是意味着可以高枕无忧


class UseInt(int):
    pass

u = UseInt()
print type(u) is types.IntType  # False

'''
上面的代码的你也可以看出来，即使是继承自int，这种基于内建类型扩展的用户自定义类型，type函数返回值也是不正确的。
还有一个问题就是古典类型的返回值都是一样的，都是indtance
'''

print isinstance(2, float)
# todo 这里有一个问题，前面发现有一种类型是另一种类型的子，然后这里忘记怎么处理了，以后遇到再说
print isinstance(int, float)
print isinstance("a", (str, unicode))
print isinstance((2, 3), (str, list, tuple))
