# coding: utf-8
"""
建议60：区别__getattr__()和__getattribute__()方法

它们都可以用做实例属性的获取和拦截（仅对实例属性有效，非类属性）
__getattr__()适用于未定义的属性
__getattribute__()对于所有属性的访问都会调用，仅应用于新式类，默认自带，要么返回属性值，要么抛出异常
如果在新式类中定义了__getattr__()，有2种情况会被调用：一是它在__getattribute__()抛出异常时，被调用;
二是在__getattribute__()中显示调用__getattr__()
"""


class ClassA:

    x = 'test x'

    def __getattr__(self, item):
        print('__getattr__')

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            raise


a = ClassA()
print(a.x)
print(a.y, '\n')
# test x
# __getattr__
# None


# __getattr__()有一个隐藏陷阱
class A(object):
    def __init__(self, name):
        self.name = name
        self.x = 20

    def __getattr__(self, name):
        print('calling __getattr__: ', name)
        if name == 'z':
            return self.x**2
        elif name == 'y':
            return self.x**3

        # raise AttributeError  # python3, python2
        # raise TypeError  # python2

    def __getattribute__(self, attr):
        try:
            return super(A, self).__getattribute__(attr)
        except KeyError:
            return 'default'


a = A('attribute')
print(a.name)
print(a.z)
if hasattr(a, 't'):  # 隐藏陷阱，自动设置属性t，其值为None，结果返回为True，调用__getattribute__
    c = a.t
    print(c, '\n')
else:
    print('instance a has no attribute t', '\n')  # 如果要执行这句，必须在__getattr__中raise AttributeError
# attribute
# calling __getattr__:  z
# 400
# calling __getattr__:  t
# calling __getattr__:  t
# None


# property和getattribute顺序
class A(object):
    _c = 'test'

    def __init__(self):
        self.x = None

    @property
    def a(self):
        print('using property to access attribute')
        if not self.x:
            print('return value')
            return 'a'
        else:
            print('error occured')
            raise AttributeError

    @a.setter
    def a(self, value):
        self.x = value

    def __getattr__(self, name):
        print('using __getattr__ to access attribute')
        print(('attribute name: ', name))
        return 'b'

    def __getattribute__(self, name):
        print('using __getattribute__ to access attribute')
        return object.__getattribute__(self, name)


a1 = A()
print(a1.a)
print('-' * 20)
a1.a = 1
print(a1.a)
print('-' * 20)
print(A._c)
# using __getattribute__ to access attribute
# using property to access attribute
# using __getattribute__ to access attribute
# return value
# a
# --------------------
# using __getattribute__ to access attribute
# using property to access attribute
# using __getattribute__ to access attribute
# error occured
# using __getattr__ to access attribute
# ('attribute name: ', 'a')
# b
# --------------------
# test
