# coding: utf-8
"""
建议67：基于生成器的协程及greenlet
"""


# 简单例子
def consumer():
    while True:
        line = yield
        print(line)


def producter():
    with open(__file__) as f:
        for i, line in enumerate(f, 1):
            yield line
            print('processed line %d' % i)
            if i >= 3:
                break


c = consumer()
c.send(None)  # or next(c)
# c.send(1)
# can't send non-None value to a just-started generator

for line in producter():
    c.send(line)


# 复杂一点
# 每个学生有3门功课成绩，统计他们的总分
# 举的这个例子有点乱，不好看
# 本意想推出yield from，但代码里又不写出来
def accumulate():
    tally = 0
    while True:
        tally += yield tally


print()
list_total = []
students = [[5, 6, 7], [8, 9, 10]]
for s in students:
    a = accumulate()
    a.send(None)
    for c in s:
        t = a.send(c)
    list_total.append(t)

a = accumulate()
a.send(None)
for s in list_total:
    t = a.send(s)
print(t)


# 更简化的办法
# 直接用yield就好，yield from其实只是一个中介跳板，还得靠生成器自己实现运算逻辑
def _accumulate():
    tally = 0
    while True:
        tally += yield tally


def accumulate():
    yield from _accumulate()


a = _accumulate()
# a = accumulate()  # 这里用yield from
a.send(None)

for s in students:
    for klass in s:
        ret = a.send(klass)

print(ret)
