# coding: utf-8
"""
建议18：构建合理的包层次来管理module

补充
在python3.5下，import Package01时，
如果Package01下的__init__.py里面写 from Module01 import Test，会提示找不到Module01模块，
正确的写法是使用相对路径 from .Module01 import *
而python2下，两种方法都是正确的。
注意，相对路径只能存在包中，如果单独运行脚本会提示错误

在__init__.py中定义 __all__ 变量，控制需要导入的子包或者模块，那么在 from package import * 时，
就会导入 __all__ 里的内容，可以在ipython中，输入dir()来验证当前命名空间引入哪些变量名
"""

import Package01

from Package01 import Module01

import Package01.Module01

from Package01 import Subpackage01

from Package01.Subpackage01 import Module01

from Package01 import Test
