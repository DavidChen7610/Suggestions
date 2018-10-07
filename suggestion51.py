# coding: utf-8
"""
建议51：用mixin模式让程序更加灵活

经python2.7和python3.5测试，原文表述__bases__有误，实例是没有__bases__属性的，只有类才有这个属性。
动态生成新类，只能用type(name, bases, dict)来实现。
"""


class KungfuTeapot(object):
    def put_in_tea(self):
        print('put in tea')

    def put_in_water(self):
        print('put in water')


class Coffeepot(object):
    def put_in_coff(self):
        print('put in coff')

    def put_in_water(self):
        print('put in water')


class People(object):
    def make_tea(self):
        teapot = self.get_teapot()
        teapot.put_in_tea()
        teapot.put_in_water()
        return teapot


class UseKungfuTeapot(object):
    def get_teapot(self):
        return KungfuTeapot()


class UseCoffeepot(object):
    def get_coffeepot(self):
        return Coffeepot()


def boss():
    bases = (
        People,
        UseKungfuTeapot,
        UseCoffeepot,
    )
    Boss = type('Boss', bases, {})
    people = Boss()
    return people


people = boss()
people.make_tea()
