# coding: utf-8
"""
建议44：理解模块pickle优劣
pickle最主要的两个函数对为dump()和load()，分别用来进行对象的序列化和反序列化。
还有dumps()和loads()
pickle.dump(obj, file, protocol=None, *, fix_imports=True)
pickle.dumps(obj, protocol=None, *, fix_imports=True)

pickle存在以下一些限制：
pickle不能保证操作的原子性。发生异常时，可能部分数据保存
pickle存在安全性问题，unpickle时有可能存在恶意代码
pickle协议是python特定的，不同语言之间的兼容性难以保障。
"""

# pickle在还原实例对象的时候一般是不调用__init__()函数的，如果要调用__init__()进行初始化，
# 对于古典类可以在类定义中提供__getinitargs__()函数，unpickle时调用__init__()，
# 并把__getinitargs__()中返回的元组作为参数传递给__init__()
# 对于新式类可以提供__getnewargs__()函数，unpickle时以class.__new__(class, *arg)的方式创建对象。

# 对于不可序列化的对象，如sockets，文件句柄，数据库连接等，也可以通过实现pickle协议来解决，
# 主要是通过特殊方法__getstate__()和__setstate__()来返回实例在被pickle时的状态。

import pickle


class TextReader:
    def __init__(self, filename):
        self.filename = filename  # 文件名称
        self.file = open(filename)  # 文件句柄
        self.position = self.file.tell()  # 文件指针位置

    def readline(self):
        line = self.file.readline()
        self.position = self.file.tell()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return '%i: %s' % (self.position, line)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        print(state)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename)
        self.file = file


reader = TextReader('zen.txt')
print(reader.readline())
print(reader.readline())
s = pickle.dumps(reader)
new_reader = pickle.loads(s)
print(new_reader.readline())


# 能够自动维护对象间的引用，如果一个对象上存在多个引用，pickle后不会改变对象间的引用，并且能够自动处理循环和递归引用。
a = ['a', 'b']
b = a
b.append('c')
p = pickle.dumps((a, b))
a1, b1 = pickle.loads(p)
print(a1, b1)
# ['a', 'b', 'c'] ['a', 'b', 'c']
a1.append('d')
print(a1, b1)
# ['a', 'b', 'c', 'd'] ['a', 'b', 'c', 'd']
