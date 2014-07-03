# -*- coding: utf-8 -*-
__author__ = 'florije'
from timeit import Timer

print Timer('temp = x;x = y;y = temp', 'x = 2;y = 3').timeit()
print Timer('x, y = y, x', 'x = 2;y = 3').timeit()

'''
1/先计算右边的表达式y,x，因此先在内存中创建元组(y, x)其标示符和值分别是y, x和其分别的值。其中y和x是在初始化时就已经存在于内存中的对象。
2/计算表达式左边的值并进行赋值，元组被依次分配给左边的标示符，通过拆包，不多解释，
'''
