# coding: utf-8
"""
建议65：熟悉python的迭代器协议

协议简单归纳如下：
1、实现__iter__()方法，返回一个迭代器。
2、实现__next__()方法，返回当前的元素，并指向下一个元素的位置，如果当前位置已无元素，则抛出StopIteration异常
"""
"""
对于容器而言，__iter__()方法返回一个迭代器对象，而对迭代器而言，它的__iter__()方法返回其本身

学习itertools的各种常用方法
"""
alist = [1, 2, 3]
it = iter(alist)  # 调用list的__iter__()
it2 = iter(it)  # 调用迭代器的__iter__()
assert id(it) == id(it2)  # 两者相等


class Fib(object):
    def __init__(self):
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a


# 把生成器和条件计算分解组合，形成各容易理解的单元
for i, f in enumerate(Fib(), 1):
    print(i, f)
    if i >= 5:
        break
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
