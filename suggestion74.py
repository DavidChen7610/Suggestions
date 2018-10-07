# coding: utf-8
"""
建议74：为包编写单元测试

unittest将递归查找当前目录下匹配test*.py模式的文件，并将其中unittest.TestCase的所有子类都实例化，
解决了”通过一条命名运行全部测试用例“的问题。
python3 -m unittest discover
"""


class MyCal(object):
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


import unittest


class MyCalTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(MyCal.add(-1, 7), 6)


if __name__ == '__main__':
    unittest.main()
