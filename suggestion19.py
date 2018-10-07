# coding: utf-8
"""
建议19：有节制地使用from ... import 语句

Python提供了3种方式来引入外部模块：
import xxx
from...import...
__import__('xxx')

一般情况下尽量优先使用import a形式
有节制地使用from a import B形式
尽量避免使用from a import *

在加载一个模块的时候，解释器实际上要完成以下动作：
1，在sys.modules中进行搜索看看该模块是否已经存在，如果存在，则将其导入到当期那局部命名空间，加载结束。
2，如果在sys.modules中找不到对应模块的名称，则为需要导入的模块创建一个字典对象，并将该对象信息插入sys.modules中。
3，加载前确认是否需要对模块对应的文件进行编译，如果需要则先进行编译。
4，执行动态加载，在当前模块的命名空间中执行编译后的字节码，并将其中所有的对象放入模块对应的字典中。

需要注意的是，直接使用import 和使用from a import B形式这两者存在一定的差异，后者直接将B暴露在当前局部空间，
而将a加载到sys.modules集合。
"""
