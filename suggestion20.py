# coding: utf-8
"""
建议20：优先使用absolute import来导入模块

相对引用有两种：一是.表示当前路径，二是..表示上层路径
原文对相对引用表述不正确。

以 Package01/Module02.py 作参考
Package01
 ├─Subpackage01
 │  ├─__init__.py
 │  ├─Module01.py
 │  └─Module02.py
 ├─__init__.py
 ├─Module01.py
 └─Module02.py

分别运行
python3 Package01/Module02.py
python3 -m Package01.Module02

python3 Package01/Module02.py
输出:
__main__

[
    'C:\\Users\\Administrator\\Desktop\\Suggestions\\Package01',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages'
]

Traceback (most recent call last):
  File "Package01/Module02.py", line 7, in <module>
    from .Module01 import Test  # noqa
ModuleNotFoundError: No module named '__main__.Module01'; '__main__' is not a package


python3 -m Package01.Module02
输出:
__main__

[
    '', 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages'
]

[
    '', 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36',
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages'
]


通过对比显示结果
python3 Package01/Module02.py __name__值为__main__
python3 -m Package01.Module02 __name__值为__main__

python3 Package01/Module02.py 搜索路径是绝对路径'C:\\Users\\Administrator\\Desktop\\Suggestions\\Package01'
python3 -m Package01.Module02 搜索路径是相对路径''（即当前运行的路径'C:\\Users\\Administrator\\Desktop\\Suggestions'）

python3 Package01/Module02.py 在运行 from .Module01 import Test时报错，认为__main__并不是一个包
python3 -m Package01.Module02 能正确认识Module01

若修改 from .Module01 import Test 为 from Module01 import Test
python3 Package01/Module02.py 分析同上
python3 -m Package01.Module02 分析同上

python3 Package01/Module02.py 搜索路径同上分析
python3 -m Package01.Module02 搜索路径同上分析

python3 Package01/Module02.py 在搜索路径上能发现Module01，运行不会出错
python3 -m Package01.Module02 在搜索路径上没有发现Module01，运行出错，"ModuleNotFoundError: No module named 'Module01'"
"""
