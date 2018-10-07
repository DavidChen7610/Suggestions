# coding: utf-8
"""
建议35：分清staticmethod和classmethod的适用场景

Python中的静态方法staticmethod和类方法classmethod都依赖于装饰器decorator来实现，其中静态方法的用法如下：
静态方法：
class C(object):
    @staticmethod
    def f(arg)
类方法:
class C(object):
    @classmethod
    def(cls, arg)

静态方法和类方法都可以通过类名，方法名或者实例方法名的方式来进行访问，其中静态方法没有常规方法的特殊行为，例如绑定，非绑定，隐式参数等规则
而类方法的调用使用类本身作为其隐含参数，单调用本身并不需要显示提供该参数。
"""
