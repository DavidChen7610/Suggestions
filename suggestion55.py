# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
很多Pythoner会有这样的误解，认为__init__()方法是类的构造方法，因为从表面上看它确实很像构造方法：
当需要实例化一个对象的时候，使用a=Class(args...)便可以返回一个类的实例，可是事实是怎么样的呢？看例子：
'''


class A(object):
    def __new__(cls, *args, **kwargs):
        print cls
        print args
        print kwargs
        print '-' * 20
        instance = object.__new__(cls, *args)
        print instance

    def __init__(self, a, b):
        print 'init gets called!'
        print 'self is', self
        self.a, self.b = a, b

# a1 = A(1, 2)
# print a1.a
# print a1.b

'''
result:
<class '__main__.A'>
(1, 2)
{}
--------------------
<__main__.A object at 0x02151670>
Traceback (most recent call last):
  File "D:/Projects/python/Suggestions/suggestion55.py", line 25, in <module>
    print a1.a
AttributeError: 'NoneType' object has no attribute 'a'
'''

'''
我们原本期望的是能够正确的输出a和b的值，可是运行却抛出了异常，除了异常外还有来自对__new__()方法调用所产生的输出，
可是我们明明没有直接调用__new__()方法，原因在哪里？实际上__init__()并不是真正意义上的构造方法，它所作的工作是在类的对象创建好
之后进行变量的初始化，__new__()方法才会真正的创建实例，是类的构造方法。
这两个方法都是object类中默认的方法，继承自object的新式类，如果不覆盖这两个方法，将会默认调用object中对应的方法，上面的程序
抛出异常是因为__new__()方法没有显示返回对象，因此实际上a1，是None，当去访问实例属性a时，就会抛出属性错误的异常。
这里我们来看一下__new__()方法和__init__()方法的定义。
object.__new__(cls[, args...])其中cls代表类，args为参数列表。
object.__init__(self[, args...])其中self代表实例对象，args为参数列表。
这两个方法之间有些不同，总结如下：
__new__()方法是静态方法，而__init__()方法是实例方法。
__new__()方法一般需要返回类的对象，当返回类的对象时将会自动调用__init__()方法进行初始化，如果没有对象返回，则__init__()方法不会被调用
__init__()方法不需要显示返回，默认为None，否则会在运行时抛出TypeError。
当需要控制实例创建的时候可使用__new__()方法，而控制实例初始化的时候使用__init__()方法。
一般情况下不需要覆盖__new__()方法，但当子类继承自不可变类型，如str，int，unicode或者tuple的时候，往往需要覆盖该方法。

当需要覆盖__new__()和__init__()方法的时候，这两个方法的参数必须保持一致，如果不一致将导致异常：
'''


class Test(object):
    # def __new__(cls, x):  # 这里会提示有问题
    #     return super(Test, cls).__new__(cls)

    def __new__(cls, x, y):
        return super(Test, cls).__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
前面都说了，一般情况下覆盖__init__()
'''