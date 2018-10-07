# coding: utf-8
"""
建议10：充分利用Lazy evaluation
延迟计算，或者惰性计算，指的就是仅仅在真正需要执行的时候才会计算表达式的值，
充分利用lazy evaluation的特性带来的好处就是主要体现在以下方面：
1，避免不必要的计算，带来性能上的提升。
if x and y，只要x为False，则不用计算y
if x or y，只要x为True，则不用计算y

2，节省空间，使得无限循环的数据结构成为可能
Python中最典型的使用延迟计算的例子就是生成器表达式了。
"""
from time import time

abbreviations = ['cf.', 'e.g', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']
list_test = ['Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.']


# 版本一
def run1():
    t = time()
    for i in range(1000000):
        for w in list_test:
            if w in abbreviations:
                pass
    return time() - t


# 版本二，优化
def run2():
    t = time()
    for i in range(1000000):
        for w in list_test:
            if w[-1] == '.' and w in abbreviations:  # if x and y ，如果x为false，则不用计算y，缩减时间
                pass
    return time() - t


print("run1() cost time:", run1())
print("run2() cost time:", run2())


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


from itertools import islice  # noqa
print(list(islice(fib(), 5)))
