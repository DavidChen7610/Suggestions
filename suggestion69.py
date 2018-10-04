"""
建议69：对象的管理与垃圾回收

"""


class Leak(object):
    def __init__(self):
        print('object with id %d was born' % id(self))


if __name__ == '__main__':
    import gc
    collected = gc.collect()  # 显示所有收集和销毁的对象的数目
    print('Garbage collector befor running: collected %d objects.' % collected)
    print('Creating reference cycles...')
    A = Leak()
    B = Leak()
    A.b = B
    B.a = A
    A = None
    B = None
    collected = gc.collect()
    print(gc.garbage)  # 显示不可达的垃圾对象的列表
    print('Garbage collector after running: collected %d objects.' % collected)
