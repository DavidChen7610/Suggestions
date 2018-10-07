# coding: utf-8
"""
建议50：利用模块实现单例模式
"""

import threading


# 注意子类的__new__覆盖父类，以及子类__init__被调用次数
class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kv):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
            return cls.objs[cls]
        finally:
            cls.objs_locker.release()


class Singleton2(Singleton):
    def __init__(self):
        print('calling __init__()')


a = Singleton2()
b = Singleton2()
print(id(a) == id(b))
# 子类调用了2次__init__()
# calling __init__()
# calling __init__()
# True


# Borg模式，所有实例共享状态
class Borg(object):
    __share_state = {}

    def __init__(self):
        self.__dict__ = self.__share_state


a, b = Borg(), Borg()
a.a = 123
print(a.a, b.a)
print(id(a.a), id(b.a))
