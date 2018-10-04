# coding: utf-8

"""
建议86：使用不同的数据结构优化性能

list的插入操作非常耗时，可以用deque来代替

序列容器获取其中的极大值或极小值元素，可以使用heapq模块
heapify()把一个序列容器转化为一个堆。
heappush() 插入元素
heappop() 删除元素
heappushpop(heap, item) 先插入新元素再获取最小元素
heapreplace(heap, item) 先获取最小元素，再插入新元素
merge() 将多个有序列表并为一个有序列表（返回迭代器，不占用内存）
nlargest() 返回无序列表中最大值
nsmallest() 返回无序列表中最小值
"""


import heapq
import random
alist = [random.randint(0, 100) for i in range(10)]
print(alist)

heapq.heapify(alist)
print(alist)

print(heapq.heappop(alist))
print(alist)
