# coding: utf-8
"""
建议22：使用with自动关闭资源

with语法还支持嵌套的方式，支持多个with语句他们两者可以相互的转换，with expr1 as e1, expr2 as e2:
等价于
with expr1 as e1:
    with expr2 as e2:

python提供contextlib模块，其中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制。
"""

import contextlib


@contextlib.contextmanager
def foo():
    try:
        print('<head>')
        yield
        print('</head>')
    except TypeError as e:
        print(e)


with foo():
    print('\tTesting')
    raise TypeError('raise error')

# <head>
#         Testing
# raise error
