# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

'''
Python 内建的字符串有两种类型，str和Unicode，它们拥有共同的祖先，basestring，其中Unicode是Python2.0中引入的一种新的数据类型，
所有的Unicode字符串都是Unicode类型的实例，创建一个Unicode字符相对简单。
'''

str_unicode = u'unicode'
print str_unicode

print type(str_unicode)

print type(str_unicode).__bases__

'''
Python中为什么需要加入对Unicode的支持呢？我们先来了解下Unicode的背景：
在Unicode之前，最早是用ASCII编码，也就是一个字节来表示，8bit，然后最高位是0，但是世界上显然不是只有一种语言，这样的结果就是即使对ASCII
编码进行拓展也不行，
'''

print 2 ** 8  # 256

'''
最常见的是utf-8，然后他的特点是对不同范围的字符使用不同长度的编码，
'''

filehande = open('test.txt', 'r')
print filehande.read()
filehande.close()

s = 'python 中文测试'
print s

'''
这里解决的方法就是先decode然后再encode，decode就是按照你保存文件的方式进行解码，然后再次编码成需要的格式，以为python自己默认的就是使用
ascii进行解码，假如不对的话，那就是乱码。一定要记清楚这些事情。
'''

import sys
print sys.getdefaultencoding()

# 补充
# 可以使用标准库里的chardet的detect方法来检测字符串的编码方式
# import chardet
# chardt.detect('中文测试')

# python2.6之后可以通过import unicode_literals自动将普通字符串识别为unicode字符串,与python3保持一致
# 不过它与chardet有冲突
from __future__ import unicode_literals
s = '中文测试'
