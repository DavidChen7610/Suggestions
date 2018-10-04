# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
'''
如果你了解Javascript或者PHP等，那么你一定对eval()有所了解，如果你没有结果过也没有关系，eval()函数非常简单。
eval("1+1==2")
类似上面的表达式
python中eval()函数讲字符串str当成有效的表达式来求值并返回计算结果，其函数声明如下:
eval(expression[, globals[, locals]])
其中参数globals为字典形式，locals为任何映射对象，他们分别表示全局和局部命名空间，如果传入global参数的字典中缺少__builtins__
的时候，当前的全局命名空间将作为globals参数输入并且在表达式计算之前被解析，locals参数默认与globals相同，如果两者都省略的话，
表达式将在eval()调用的环境中执行。
eval is evil，这是一句广为人知的对于evla()的评价，它主要针对的时eval的安全性，那么eval存在什么样的安全漏洞呢？
'''

import sys
from math import *


def ExpCalcBot(user_func):
    try:
        print('Your answer is ', eval(user_func))
    except NameError:
        print('The expression you enter is not valid')


print('Hi, I am ExpCalcBot, please input your expression or enter e to end.')
input_str = ''
while 1:
    print('Please enter a number or operation. Enter c to complete. :')
    input_str = input()
    if input_str == str('e'):
        sys.exit()
    elif repr(input_str) != repr(''):
        ExpCalcBot(input_str)
        input_str = ''
    else:
        break
'''
Hi, I am ExpCalcBot, please input your expression or enter e to end.
Please enter a number or operation. Enter c to complete. :
1+sin(20)
Your answer is  1.91294525073
Please enter a number or operation. Enter c to complete. :
__import__("os").system("dir")
Your answer is sh: dir: command not found
 32512
Please enter a number or operation. Enter c to complete. :
__import__("os").system("ls")
Your answer is README.md
const.py
notest.py
others
suggestion01
suggestion01.py
suggestion02.py
suggestion03.py
suggestion04.py
suggestion05.py
suggestion06.py
suggestion07.py
suggestion08.py
suggestion09.py
suggestion10.py
suggestion11.py
suggestion12.py
suggestion13.py
suggestion14.py
test.txt
 0
Please enter a number or operation. Enter c to complete. :
'''
'''
上面的还是善意的，假如真的恶意的比如:
__import__("os").system("del * /Q")
这该是多么危险的事情，然后你可能会说那我还有globals参数呢，我直接用该参数禁止访问就可以了，那么我就按照你说的做一下
'''


def ExpCalcBot_re(user_func):
    try:
        math_fun_list = ["sin", "cos"]
        math_fun_dict = dict([(k, globals().get(k)) for k in math_fun_list])
        print('Your answer is ', eval(user_func))
    except NameError:
        print('The expression you enter is not valid')


# 然后你看结果发现确实有效果，真的么？
# [c for c in ().__class__.bases__(0).__subclasses__() if c.__name__ == 'Quitter'][0](0)()
# ().__class__.bases__(0).__subclasses__() 是用来返回object的所有子类，quitter类绑定quit方法，所以上面的这个直接导致程序退出。
'''
总而言之，对于有经验的侵入者来说，他可能会有一系列的的强大的手段，使得eval()函数可以解释和调用这些方法，从而带来更大的破坏，此外
eval()函数也给程序的调试带来一定的困难，要查看他运行的函数内容太困难了。因此在实际应用中如果使用对象不是信任源，应该尽量避免使用
在需要使用eval的地方可以使用安全性更好的ast.literal_eval替代
'''

# 补充
# ast.literal_eval
# Safely evaluate an expression node or a string containing a Python
# expression.  The string or node provided may only consist of the following
# Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
# sets, booleans, and None.

from ast import literal_eval

a = literal_eval('[1, 2]')
print(type(a))  # <class 'list'>
b = literal_eval('{"a":1, "b":2}')
print(type(b))  # <class 'dict'>
c = literal_eval('11')
print(type(c))  # <class 'int'>
d = literal_eval('__import__("os").system("ls")')
# Traceback (most recent call last):
#   File "suggestion14.py", line 116, in <module>
#     d = literal_eval('__import__("os").system("ls")')
#   File "/usr/lib/python3.5/ast.py", line 84, in literal_eval
#     return _convert(node_or_string)
#   File "/usr/lib/python3.5/ast.py", line 83, in _convert
#     raise ValueError('malformed node or string: ' + repr(node))
# ValueError: malformed node or string: <_ast.Call object at 0x7fcc61cad780>
