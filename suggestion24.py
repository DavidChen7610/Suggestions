# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
遵循异常处理的几点基本原则
'''

'''
现实生活是不完美的，意外和异常会在不经意间发生，从而使我们的生活不得不暂时偏离正常轨道，软件世界也是如此，或因为外部原因，或者因为内部原因，
程序会在某些条件下产生异常或者错误，为了提高系统的健壮性和用户的友好性，需要一定的机制来处理这种情况，跟其他很多编程语言一样，Python也提供
了异常处理机制，Python中常用的异常处理语法是try,except, else,finally，他们可以有多种组合，
try-except, try-except-else, try-finally以及try-except-else-finally
'''

'''
异常处理的话，需要注意以下的几点：
1.注意异常的粒度，不推荐在try中放入过多的代码，异常的烈度是人为划分的，在处理异常的时候最好保持异常粒度的一致性和合理性，同时要避免在try
中放入过多的代码，即避免异常粒度过大，在try中放入过多的代码带来的问题是如果程序中抛出异常，将会比较难定位，给debug和修复带来不便，因此应
尽量只在可能抛出异常的语句块前面放入try语句。
2.谨慎使用单独的except语句处理所有异常，最好能定位到具体的异常，同样也不推荐使用except Exception或者except StandardError来捕获异常。
'''

import sys
try:
    print a
    b = 0
    print a/b
except:
    sys.exit('ZeroDivisionError:Can not division zero')

'''

'''

