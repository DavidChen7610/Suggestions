# -*- coding: utf-8 -*-
__author__ = 'florije'
from timeit import Timer

print Timer('temp = x;x = y;y = temp', 'x = 2;y = 3').timeit()
print Timer('x, y = y, x', 'x = 2;y = 3').timeit()

'''
1/先计算右边的表达式y,x，因此先在内存中创建元组(y, x)其标示符和值分别是y, x和其分别的值。其中y和x是在初始化时就已经存在于内存中的对象。
2/计算表达式左边的值并进行赋值，元组被依次分配给左边的标示符，通过拆包，不多解释，
'''

# 补充：
# 不用引入Timer类，直接用timeit函数，就可以了，它会创建一个Timer，再执行类方法timeit
# 在ipython中，timeit是个魔术函数，它是ipython的内置命令，与timeit模块的timeit函数有着相似的功能，区别是timeit支持命令行形式
# Usage, in line mode:
#   %timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] statement
# or in cell mode:
#   %%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] setup_code
#   code
#   code...
