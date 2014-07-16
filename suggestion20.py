# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
假设有如下文件机构，其中
'''

import codecs


# def rot13(string):
# # codecs.encode(string, 'rot_13')
#     return string.encode('rot13')


def rot13(string, offset):
    def encode_char(ch):
        asc = ord(ch)
        if (asc > 96) and (asc < 123):
            return chr((asc - 97 + offset).__mod__(26) + 97)
        elif (asc > 64) and (asc < 91):
            return chr((asc - 65 + offset).__mod__(26) + 65)
        else:
            return ch

    temp = ''
    for char in string:
        temp = '%s%s' % (temp, encode_char(char))
    return temp


if __name__ == '__main__':
    # s = rot13('fuboqing')
    # print s
    # print rot13(s)


    tmp = rot13('fuboqing', 13)
    print tmp
    print rot13(tmp, 13)



'''
优先使用absolute import来导入模块
假设有这种结构呢，就是app下有sub1和sub2的包，然后sub1下面有mod1.py以及string.py在sub2下面有mod2.py
那么当在mod1.py中import string的时候,然后再引用string.lower()方法，到底引用的是sub1/string.py中的lower方法还是Python标准库中的
string里面的lower()方法呢？
通过查看发现，很明显是直接从本目录下面得到的。
也就是说解释器默认先从当前目录下面搜索对应的模块，当搜到string.py的时候就停止了。
那要是我想使用Python自带的string模块中的方法，该怎么实现呢？
这里的解决方案就是absolute import和relative import相关的话题
'''

'''
在Python2.4以前，默认的是隐式的relative import，局部范围的模块将覆盖同名的全局范围的模块，如果要使用标准库中同名的模块，
你不得不去深入考察sys.modules一番，显然这并不是一种非常友好的做法，Python2.5以后，虽然仍旧默认的是relative import但是它为absolute
import提供了一种新的机制，在模块中使用from __future__ import absolute_import语句进行说明后再进行导入，同时他还通过点号提供了一种
显示进行relative import的方法，'.'表示当前目录，'..'表示当前目录的上一层目录，

当时事情不是这么就容易解决的，使用显示relative import之后再运行程序一不小心你就可能会遇到这样的错误，
ValueError:Attempted relative import in nonpackage
这是什么原因呢？这个问题产生的原因是在于relative import使用模块的__name__属性来决定当前模块在包层次结构中的位置，如果当前的模块名称中不
包含任何包的信息，那么它将默认为模块在包的顶层位置，而不管模块在文件系统的实际位置，而在relative import的情形下，__name__会随着文件
加载方式的不同而发生改变，上例中如在目录app/sub1/下运行的Python mod1.py会发现模块的__name__为__main__.但是在目录app/sub1/下运行
Python -m mod1.py 会发现__name__变为mod1，其中-m

'''
