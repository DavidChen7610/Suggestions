# -*- coding: utf-8 -*-
__author__ = 'florije'

print [(i % 3 == 0) or i for i in xrange(1, 100)]

string = 'please input your sentense'
print [item for item in reversed(string.split())]
