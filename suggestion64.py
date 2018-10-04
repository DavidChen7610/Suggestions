"""
建议64：利用操作符重载实现中缀语法
安装pipe库，这个库核心代码只有几行，就是重载了__xor__()方法
我把pipe库放在项目中，改名为_pipe.py
"""


class Pipe(object):
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, pred):
        return Pipe(lambda x: self.function(x, pred))


@Pipe
def where(iterable, predicate):
    return (x for x in iterable if (predicate(x)))


s = [1, 2, 3] | where(lambda x: x == 2)
print(list(s))
# [2]

"""
代码分析：
@Pipe
def where(iterable, predicate):
    ...
等价于
where = Pipe(where))
其中 where.function = where

where(lambda x: x == 2)
等价于
where.__call__(lambda x: x == 2)
    return Pipe(lambda x: where.function(x, lambda x: x == 2))
新的实例记名为obj
其中 obj.function = lambda x: where.function(x, lambda x: x == 2)

当 [1, 2, 3] | where(lambda x: x ==2) 时
等价于
obj.__ror__([1, 2, 3])
    return obj.function([1, 2, 3])
        return where.function([1, 2, 3], lambda x: x == 2)
            return (x for x in [1, 2, 3] if lambda x: x == 2)
至此结束

注意一点：
[1, 2, 3] 和 lambda x: x * 2 都是函数where的两个参数
"""


"""
注意pipe库是惰性求值的
"""
from _pipe import *
ret = [1, 2, 3, 4, 5] | where(lambda x: x % 2) | tail(2) | select(lambda x: x * x) | add
print(ret)
