# coding: utf-8
"""
建议23：使用else子句简化循环（异常处理）

除了if...else...
还有以下用法：
for...else...
try...else...
"""

# 当for没有中断跳出的话，则运行else
for i in range(10):
    if i == 15:
        break
else:
    print(i)


# 当try没有抛出异常的话，则运行else
try:
    # raise ValueError('can not be 0')
    3 / 2
except ValueError as e:
    print(e)
else:
    print('ok')
