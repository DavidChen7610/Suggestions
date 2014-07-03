# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
Lazy evaluation常被译作延迟计算，或者惰性计算，指的就是仅仅在真正需要执行的时候才会计算表达式的值，充分利用lazy evaluation的特性带来的
好处就是主要体现在以下方面：
1/避免不必要的计算，带来性能上的提升。
2/
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

    def exist_files(self, files):
        '''
        判断文件是否存在
        :param file_names: "test1.txt,test2.txt"
        :return:list [(test1.txt:True), (test2.txt:False)]
        '''
        if not files:
            raise Exception('file_name is %s' % files)
        return [(item.strip(), os.path.exists(item.strip())) for item in files.split(',')]
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


if __name__ == '__main__':
    res = FileUtils().exist_files('test.txt, test1.txt')
    print res
    for item in res:
        if item[1]:
            print item[0]