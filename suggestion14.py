# coding: utf-8
"""
建议14：警惕eval()的安全漏洞

eval is evil，这是一句广为人知的对于evla()的评价，它会让恶意代码得以执行。
此外，eval()函数也给程序的调试带来一定的困难，要查看他运行的函数内容太困难了。
因此在实际应用中如果使用对象不是信任源，应该尽量避免使用。
在需要使用eval的地方可以使用安全性更好的ast.literal_eval替代。

ast.literal_eval
Safely evaluate an expression node or a string containing a Python
expression.  The string or node provided may only consist of the following
Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
sets, booleans, and None.
"""

# 列出当前目录下的所有文件
eval('__import__("os").system("ls")')  # for linux
# eval('__import__("os").system("dir")')  # for windows

from ast import literal_eval  # noqa

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
