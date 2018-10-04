# coding: utf-8
"""
建议51：用mixin模式让程序更加灵活
"""


class People(object):
    def make_tea(self):
        teapot = self.get_teapot()
        teapot.put_in_tea()
        teapot.put_in_water()
        return teapot


class UseSimpleTeapot(object):
    def get_teapot(self):
        return SimpleTeapot()


class UseKungfuTeapot(object):
    def get_teapot(self):
        return KungfuTeapot()


class UseCoffeepot(object):
    def get_teapot(self):
        return Coffeepot()


def simple_tea_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot,)
    return people


def coffee_people():
    people = People()
    people.__bases__ += (UseCoffeepot,)
    return people


def tea_and_coffee_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot, UseCoffeepot,)
    return people


def boss():
    people = People()
    type(people).__bases__ += (UseKungfuTeapot, UseCoffeepot,)
    return people


# 测试环境py2.7和py3.5，这个例子不再适用
# 这个例子有两处错误，一个是实例没有__bases__属性，只能class有，所以要转为type(xxx)；另一个致命错误是
# Cannot create a consistent method resolution order (MRO) for bases UseKungfuTeapot, object, UseCoffeepot
# 解决这个问题，可能元类是一个方向
people = boss()
