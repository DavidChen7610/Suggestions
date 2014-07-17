# -*- coding: utf-8 -*-
__author__ = 'florije'

import urllib

data = urllib.urlopen('http://www.gjjx.com.cn/')
print data.read()