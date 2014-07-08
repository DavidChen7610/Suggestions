# -*- coding: utf-8 -*-
__author__ = 'florije'

print False or 1
print False or 0
print True or 0
print True and 1
print True and 0
print False and 1

print True and 1 or 2
print False and 1 or 2

cond, a, b = True, 0, 1
print cond and a or b
# 这里会输出b的值，因为什么呢，因为第一个值是布尔可以认出的False
# 在 and or运算中 空字符串 ‘’，数字0，空列表[]，空字典{}，空()，None，在逻辑运算中都被当作假来处理
'''
怎么处理呢
'''
c = cond and a or (not cond or a) or b  # 这个明显不对K
print c
print (cond and [a] or [b])[0]


def iif(condition, true_part, false_part):
    return (condition and [true_part] or [false_part])[0]
