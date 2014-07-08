# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

'''
在判断两个字符是否相等的时候，混用is和==是很多初学者经常犯的错误，造成的结果是程序在不同情况下表现不一，
'''
a = "Hi"
b = "Hi"
print a == b
print a is b

a1 = "I am using long string for testing.I am using long string for testing.I am using long string for testing." \
     "I am using long string for testing."
b1 = "I am using long string for testing.I am using long string for testing.I am using long string for testing." \
     "I am using long string for testing."
print a1 == b1
print a1 is b1
print id(a1), id(b1)  # 这里应该是错误的，因为这里的话，按照python的流程应该已经超出了范围，尽量不要这么写，很危险

str1 = "string"
str2 = "".join(['s', 't', 'r', 'i', 'n', 'g'])
print str2

print str1 == str2
print str1 is str2
print id(str1), id(str2)


'''
is 表示的时对象标示符，而==表示的意思是相等，显然两者不是一个东西，实际上，造成上面输出不一致的根本原因在于：
is的作用是用来检查对象的标示符是否一致，也就是比较两个对象在内存中是否拥有同一块内存空间，它并不适合用来判断两个字符串是否相等
'''