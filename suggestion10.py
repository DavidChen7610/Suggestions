# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
Lazy evaluation常被译作延迟计算，或者惰性计算，指的就是仅仅在真正需要执行的时候才会计算表达式的值，充分利用lazy evaluation的特性带来的
好处就是主要体现在以下方面：
1/避免不必要的计算，带来性能上的提升。
2/节省空间，使得无限循环的数据结构成为可能
Python中最典型的使用延迟计算的例子就是生成器表达式了。它仅仅在每次需要计算的时候才通过yield产生所需的元素。斐波那契数列在Python中实现
起来显得很简单，而while True也不会导致其他语言中所遇到的无限循环的问题。
'''

import os


class FileUtils(object):
    def exist_file(self, file_name):
        '''

        :param file_name: test.txt
        :return:
        '''
        if os.path.exists(file_name):
            print "%s exist" % file_name
        else:
            print "%s not exist" % file_name

    def exist_files(self, files, path='.'):
        '''
        判断文件是否存在
        :param file_names: "test1.txt,test2.txt,others/test3.txt"
        :return:list [(test1.txt:True), (test2.txt:False), ('others/test3.txt', True)]
        '''
        if not files:
            raise Exception('file_name is %s' % files)
        return [(item.strip(), os.path.exists(os.path.join(path, item.strip()))) for item in files.split(',')]
        # res_dict = {}
        # for name in files:
        #     res_dict[name] = os.path.exists(name)
        # return res_dict


from time import time

t = time()
abbreviations = ['cf.', 'e.g', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']
for i in xrange(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        # if w in abbreviations:  # 在编程的时候，如果对于or
        if w[-1] == '.' and w in abbreviations:
            pass

print "total run time"
print time()-t


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
from itertools import islice
print list(islice(fib(), 5))


if __name__ == '__main__':
    res = FileUtils().exist_files('test.txt, test1.txt, others/multithread.py')
    print res
    for item in res:
        if item[1]:
            print item[0]