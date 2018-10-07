# coding: utf-8
"""
建议55：__init__()不是构造方法

很多Pythoner会有这样的误解，认为__init__()方法是类的构造方法，因为从表面上看它确实很像构造方法：
当需要实例化一个对象的时候，使用a=Class(args...)便可以返回一个类的实例，可是事实是怎么样的呢？看例子：
"""


class A(object):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        print('-' * 20)
        instance = object.__new__(cls)  # 注意，只要参数cls
        return instance

    def __init__(self, a, b):
        print('init gets called!')
        print('self is', self)
        self.a, self.b = a, b


a1 = A(1, 2)
print(a1.a)
print(a1.b)
# <class '__main__.A'>
# (1, 2)
# {}
# --------------------
# init gets called!
# self is <__main__.A object at 0x7f7393bfd518>
# 1
# 2


# 在哪些特殊情况下需要覆盖__new__()方法？
# 1、当类继承（如str,int,unicode,tuple或者frozenset等)不可变类型且默认的__new__()方法不变时，满足不了需求
# 设想将一个字符串按空格切分，只修改__init__()，结果与设想不同
class UserSet(frozenset):
    def __init__(self, arg=None):
        if isinstance(arg, str):
            arg = arg.split()
        frozenset.__init__(arg)  # 参数随意也行，完全不起作用


print(UserSet('I am testing'))
print(frozenset('I am testing'))

# UserSet({'m', ' ', 't', 'I', 'n', 'i', 'e', 'a', 'g', 's'})
# frozenset({'m', ' ', 't', 'I', 'n', 'i', 'e', 'a', 'g', 's'})


# 正确的方法是修改__new__()
class UserSet(frozenset):
    def __new__(cls, *args):
        if args and isinstance(args[0], str):
            args = (args[0].split(), ) + args[1:]
        return super().__new__(cls, *args)


print(UserSet('I am testing'))
print(frozenset('I am testing'))
# UserSet({'testing', 'I', 'am'})
# frozenset({'I', 'a', ' ', 'n', 't', 'i', 'e', 'm', 's', 'g'})


# 2、用来实现工厂模式或者单例模式或者进行元类编程，以简单工厂为例子
class Shape(object):
    def __init__(self):
        pass

    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self):
        print('I am a triangle')

    def draw(self):
        print('I am drawing triangle')


class Rectangle(Shape):
    def __init__(self):
        print('I am a rectangle')

    def draw(self):
        print('I am drawing rectangle')


class ShapeFactory(object):
    shapes = {'triangle': Triangle, 'rectangle': Rectangle}

    def __new__(cls, name):
        if name in cls.shapes:
            print('creating a new shape %s' % name)
            return cls.shapes[name]()
        else:
            print('creating a new shape %s' % name)
            return Shape()


# 函数形式
# def ShapeFactory(name):
#     shapes = {'triangle': Triangle, 'rectangle': Rectangle}

#     if name in shapes:
#         print('creating a new shape %s' % name)
#         return shapes[name]()
#     else:
#         print('creating a new shape %s' % name)
#         return Shape()

ShapeFactory('rectangle').draw()
