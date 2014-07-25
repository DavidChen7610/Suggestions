# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
分清staticmethod和classmethod的适用场景
'''
'''
Python中的静态方法staticmethod和类方法classmethod都依赖于装饰器decorator来实现，其中静态方法的用法如下：
静态方法：
class C(object):
    @staticmethod
    def f(arg)
类方法:
class C(object):
    @classmethod
    def(cls, arg)
'''
'''
静态方法和类方法都可以通过类名，方法名或者实例方法名的方式来进行访问，其中静态方法没有常规方法的特殊行为，例如绑定，非绑定，隐式参数等规则
而类方法的调用使用类本身作为其隐含参数，单调用本身并不需要显示提供该参数。
'''


class A(object):
    def instance_method(self, x):
        print 'calling instance method instance_method(%s, %s)' % (self, x)

    @classmethod
    def class_method(cls, x):
        print 'calling class_method(%s, %s)' % (cls, x)

    @staticmethod
    def static_method(x):
        print 'calling static_method(%s)' % (x,)

a = A()
a.instance_method('test')
a.class_method('test')
a.static_method('test')

'''
上面的例子看出来，类方法和静态方法的简单应用，从程序的输出可以看出虽然类方法在调用的时候没有显示的声明cls，但实际上类本身作为隐含参数
传入的
在了解完静态方法和类方法的基本知识之后再来研究这样一个问题，为什么需要静态方法和类方法，他们和普通的实例方法之间存在什么区别。我们通过对
具体的问题的研究来回答这些问题，假设有水果类Fruit，它用属性total表示总量，Fruit中已经有set()来设置总量，print_total()方法来打印水果
的数量，类Apple和类Oriange继承自Fruit，我们需要分别跟踪不同类型的水果的总量，有好几种方法可以实现这个功能。
'''

'''
1/利用普通的实例方法来实现代码
在Apple和Orange类中分别定义类变量total，然后再覆盖积累的set()和print_total()方法，但这些会导致代码的冗余，因为本质上这些方法所实现的
功能是相同的。
'''


class Fruit(object):
    total = 0

    def __init__(self, area='', category='', batch=''):
        self.area = area
        self.category = category
        self.batch = batch

    @staticmethod
    def init_product(product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = Fruit(area, category, batch)
        return fruit

    @classmethod
    def print_total(cls):
        print cls.total
        print id(Fruit.total)
        print id(cls.total)

    @classmethod
    def set(cls, value):
        print 'calling class_method(%s, %s)' % (cls, value)
        cls.total = value


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


a1 = Apple()
a1.set(200)

a2 = Apple()

o1 = Orange()
o1.set(300)

o2 = Orange()

a1.print_total()
o1.print_total()


'''
简单分析可以知道，针对不同种类的水果对象调用set()方法的时候，隐形传入的参数为该对象所对应的类，在调用set()的过程中，动态生成了对应的类的
类的类变量，这就是classmethod的妙处，那么假如改成静态方法是否可行呢？
我们再来看一个必须使用类方法而不是静态方法的例子，假设对于每一个Fruit类我们提供3个实例属性，area表示区域代码，category表示种类代码，
batch表示批次号，现在需要一个方法能够将以area-category-batch形式表示的字符串形式的输入转化为对应的属性并以对象返回。
假设Fruit中有如下初始化方式，并且有静态方法init_Product()能够满足上面的需求
'''

'''
看看会发生什么问题
'''
app1 = Apple(2, 5, 10)
org1 = Orange.init_product("3-3-9")
print 'app1 is instance of Apple:' + str(isinstance(app1, Apple))
print 'org1 is instance of Orange:' + str(isinstance(org1, Orange))

