# -*- coding: utf-8 -*-
"""
建议17：考虑兼容性，尽可能使用Unicode

Python2 内建的字符串有两种类型，str和Unicode，它们拥有共同的祖先，basestring，
其中Unicode是Python2.0中引入的一种新的数据类型，所有的Unicode字符串都是Unicode类型的实例。

Python3 内建的字符串就是unicode字符串
"""

import sys
print(sys.getdefaultencoding())

# 补充
# 可以使用标准库里的chardet的detect方法来检测字符串的编码方式
# import chardet
# chardt.detect('中文测试')

# python2.6之后可以通过import unicode_literals自动将普通字符串识别为unicode字符串,与python3保持一致
# 在python2它会与chardet有冲突
from __future__ import unicode_literals
s = '中文测试'
