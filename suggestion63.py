"""
熟悉python对象协议
因为python是一门动态语言，duck typing的概念遍布其中，只要方法的名字一样就可以调用。

类型转换协议：
__str__()
__repr__()
__init__()
__long__()
__float__()
__nonzero__()

用以比较大小的协议：
__eq__()  # ==
__ne__()  # !=
__lt__()  # <
__gt__()  # >

数值类型相关的协议
__add__             # +
__sub__             # -
__mul__             # *
__div__             # /
__floordiv__        # //
__truediv__         # /
__pow__             # **
__mod__             # %
__divmod__          # divmod()
__lshift__          # <<
__rshift__          # >>
__and__             # &
__or__              # |
__xor__             # ^
__invert__          # ~
__iadd__            # +=
__isub__            # -=
__imul__            # *=
__idiv__            # /=
__ifloordiv__       # //=
__itruediv__        # /=
__ipow__            # **=
__imod__            # %=
__ilshift__         # <<=
__irshift__         # >>=
__iand__            # &=
__ior__             # |=
__ixor__            # ^=
__pos__             # + 正
__neg__             # - 负
__abs__             # abs()
反运符：python中特有的概念，以加法为例，something+other，首先调用的是something.__add__(other)方法，如果something没有__add__()方法，它会去查
看other有没有__radd__()方法，如果有，则把something作为参数来调用，other.__radd__(something)，类似方法，所有数值运行符和位运行符都是支持的

容器类型协议
__len__()       # len()
__getitem__()   # 读
__setitem__()   # 写
__delitem__()   # 删除
__iter__()      # 迭代器协议
__reversed__()  # reversed()
__contains__()  # 容器类型中判断成员是否存在，即in和not in运行符

可调用对象协议
__call__(self)    # 类的实例，以函数的形式来调用

可哈希对象协议
__hash__(self)    # 只有支持可哈希协议的类型才能作为dict的键类型（只要继承自object的新式类默认就支持了）

描述符协议
@property

属性交互协议
__getattr__()
__setattr__()
__delattr__()

上下文管理器协议
__enter__()
__exit__()
"""


class Closer(object):
    def __init__(self, obj):
        self.obj = obj
    
    def __enter__(self):
        return self.obj  # bound to target
    
    def __exit__(self, et, ev, tb):
        try:
            self.obj.close()
        except AttributeError:  # obj isn't closable
            print('Not closable')
            return True  # exception handled successfully


with Closer(open('suggestion63.py')) as f:
    print(f.readline())

f.readline()
# 发生异常: ValueError
# I/O operation on closed file.
#   File "/home/ubuntu/Desktop/Suggestions/suggestion63.py", line 101, in <module>
#     f.readline()

"""
与这里Closer类似的类在标准库中已经存在，就是contextlib里的closing。
"""
