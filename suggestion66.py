# coding: utf-8
"""
建议66：熟悉python的生成器
生成器有两个很棒的用处，其中之一是实现with语句的上下文管理器协议，利用的是调用生成器函数时函数
体并不执行，当第一次调用next()方法时才开始执行，并执行到yield表达式后中止，直到下一次调用next()
方法这个特性；
其二是实现协程，利用send()、throw()、close()等特性
"""


def echo(value=None):
    print("Excution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = yield value
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


generator = echo(1)
print(next(generator))
print(generator.send(2))

print(generator.throw(TypeError, 'spam'))

print(generator.close())
