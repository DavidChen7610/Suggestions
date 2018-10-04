"""
建议56：理解名字查找机制
1、局部作用域 locals()
2、嵌套作用域
3、全局作用域 globals()
4、内置作用域
查找顺序：1, 2, 3, 4
"""


# 错误示例
# def foo(x):
#     a = x

#     def bar():
#         b = a * 2
#         a = b + 1
#         print(a)

#     return bar


# bar1 = foo(2)()
# Traceback (most recent call last):
#   File "suggestion56.py", line 23, in <module>
#     bar1 = foo(2)()
#   File "suggestion56.py", line 16, in bar
#     b = a * 2
# UnboundLocalError: local variable 'a' referenced before assignment

# 正确示例
def foo(x):
    a = x

    def bar():
        nonlocal a
        b = a * 2
        a = b + 1
        print(a)

    return bar


bar1 = foo(2)()
