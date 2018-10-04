"""
建议73：理解单元测试概念
遵循单元测试基本原则 ：
一致性：1000次执行和一次执行的结果是一样的。
原子性：单元测试的执行结果只有两种，True或者False
单一职责：测试基于情景和行为，而不是方法。如果一个方法对应着多种行为，应用有多个测试用例；而一个行为
即使对应多个方法也只能有一个测试用例。
隔离性：不能依赖于具体的环境设置，如数据库的访问，环境变量的设置，系统的时间等，也不能依赖于其他的测试
用例以及测试执行的顺序，并且无条件逻辑依赖。单元测试的所有输入应该是确定的，方法的行为和结果应是可以
预测的。
"""


class MyCal(object):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


import unittest


class MyCalTest(unittest.TestCase):
    def setUp(self):
        print('running set up')
        self.mycal = MyCal()

    def tearDown(self):
        print('running teardown')
        self.mycal = None

    def testAdd(self):
        self.assertEqual(self.mycal.add(-1, 7), 6)

    def testSub(self):
        self.assertEqual(self.mycal.sub(10, 2), 8)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyCalTest('testAdd'))
    suite.addTest(MyCalTest('testSub'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
