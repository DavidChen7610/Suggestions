"""
使用copy模块深拷贝对象
"""

from copy import deepcopy, copy


class A:
    def __init__(self, name):
        self.name = name
        self.order = []

    def show_detail(self):
        print('name={}, order={}'.format(self.name, self.order))

    def show_ids(self):
        print('id(name)={}, id(order)={}'.format(id(self.name), id(self.order)))


a = A('apple')
a.order.append(1)
a.order.append(2)

b = copy(a) if input('浅复制输入1，其余为深复制') == '1' else deepcopy(a)
a.show_detail()
a.show_ids()
b.show_detail()
b.show_ids()

"""
浅复制，两个对象的列表id都是相同的
name=apple, order=[1, 2]
id(name)=140048781451080, id(order)=140048751769928
name=apple, order=[1, 2]
id(name)=140048781451080, id(order)=140048751769928
"""

"""
浅复制输入1，两个对象的列表id不一样，内容是相同的
name=apple, order=[1, 2]
id(name)=140318261514168, id(order)=140318236200712
name=apple, order=[1, 2]
id(name)=140318261514168, id(order)=140318261565192
"""
