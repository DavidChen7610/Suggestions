# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
无论try语句中是否有异常抛出，finally语句总会被执行，由于这个特性，finally语句经常被用来做一些清理工作，比如打开一个文件，抛出异常后在
finally语句中对文件句柄进行关闭操作。

'''


def finally_test():
    print 'I am starting------'
    while True:
        try:
            print 'I am running!' + a
            # raise IndexError('IndexError!')
        except IndexError, e:
            print 'NameError happened %s' % e
        finally:
            print 'finally executed!'
            break
    print 'you see it!'

finally_test()

'''
result:
I am starting------
finally executed!
you see it!
'''

'''
上面的例子中try代码块抛出了IndexError异常，但是在except块却没有对应的异常声明，按常理该异常会向上层抛出，可是程序输出却没有提示任何的
异常发生，也就是IndexError异常被丢失了。
这究竟是什么原因呢？当try块中发生异常的时候，如果在except语句中找不到对应的异常处理，异常将会被临时保存起来，当finally执行完毕的时候，
临时保存的异常会再次被抛出，但如果finally语句中产生了新的异常或者执行了return或者break语句，那么临时保存的异常将会被丢失，从而导致异常
屏蔽。
这是finally使用时候要小心的第一个陷阱。
'''


def return_test(a):
    res = []
    try:
        if a <= 0:
            raise ValueError('Data can not be negative')
        else:
            res.append(a)
            return a
    except ValueError as e:
        print e
    finally:
        print 'The end!'
        res.append(-1)
        return res

print return_test(0)
print return_test(2)

'''
!!!!!这本书讲的根本就不对！！！！！！！！！！
'''

'''
result:
Data can not be negative
The end!
-1
The end!
-1
'''