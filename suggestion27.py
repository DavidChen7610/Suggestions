# coding: utf-8
"""
建议27：连接字符串应优先使用join而不是+
"""
from timeit import timeit

str1, str2, str3 = 'test1 ', 'test2 ', 'test3 '
print(str1 + str2 + str3)
print(''.join([str1, str2, str3]))
# test1 test2 test3
# test1 test2 test3

# 如果字符串数量较少，用+比较快简单
num = 10**6
print(timeit('"".join([str1, str2, str3])', 'from __main__ import str1, str2, str3', number=num))
print(timeit('ret = str1 + str2 + str3', 'from __main__ import str1, str2, str3', number=num))
# 0.33994820041815704
# 0.2149112021829882

# 如果字符串数据非常多，用join明显比+快得多，这是因为每次+都要开分配内存给临时变量，
# 而join是一次计算所需的空间，然后一次性申请所需要的内存。
strlist = ['it is a long value string will not keep in memory'] * 10000


def join_test():
    ''.join(strlist)


def plus_test():
    result = ''
    for i, v in enumerate(strlist):
        result += v


print(timeit('join_test()', 'from __main__ import join_test', number=1000))
print(timeit('plus_test()', 'from __main__ import plus_test', number=1000))
# 0.19037885782291508
# 3.5462273705246505
