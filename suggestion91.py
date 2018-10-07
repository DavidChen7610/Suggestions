# coding: utf-8
"""
建议91：使用Cython编写扩展模块

Cython是一个“编译器”，它可以把Python代码直接编译成等价的C/C++代码，从而获得性能提升。
Cython提供了无需显示编译的方案：pyximport。只要将原有的python代码后缀名从.py改为.pyx即可。

cp p1.py p1_c.pyx
cp p1.py p1_cy.pyx
cp p1.py p1_fc.pyx

ipython3
import pyximport; pyximport.install()  # 自动编译所有.pyx文件
import arithmetic  # 这时才生成so文件
arithmetic.__file__  # 查看so文件所在位置，复制so文件到在当前文件的同级目录

下面对p1.py文件进行四种方式的速度比较
使用c库函数速度最快
"""

import timeit

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000
t = timeit.Timer('p1.great_circle(%f, %f, %f, %f)' % (lon1, lat1, lon2, lat2), 'import p1')
py = t.timeit(num)
print('Pure python function %6.4f sec' % py)

t = timeit.Timer('p1_c.great_circle(%f, %f, %f, %f)' % (lon1, lat1, lon2, lat2), 'import p1_c')
c = t.timeit(num)
save = abs(c - py) / py * 100
print('python-to-c function %6.4f sec, save %4.2f%%' % (c, save))

t = timeit.Timer('p1_cy.great_circle(%f, %f, %f, %f)' % (lon1, lat1, lon2, lat2), 'import p1_cy')
cy = t.timeit(num)
save = abs(cy - py) / py * 100
print('cpython     function %6.4f sec, save %4.2f%%' % (cy, save))

t = timeit.Timer('p1_fc.great_circle(%f, %f, %f, %f)' % (lon1, lat1, lon2, lat2), 'import p1_fc')
fc = t.timeit(num)
save = abs(fc - py) / py * 100
print('from c      function %6.4f sec, save %4.2f%%' % (fc, save))

# Pure python function 1.0514 sec
# python-to-c function 0.9740 sec, save 7.36%
# cpython     function 0.7418 sec, save 29.45%
# from c      function 0.0968 sec, save 90.79%
