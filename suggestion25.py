# coding: utf-8
"""
建议25：避免finally中可能发生的陷阱

无论try语句中是否有异常抛出，finally语句总会被执行。
finally有2个陷阱，不能用return 或 break
"""


# 没有处理的异常被丢弃没有向上抛出，有时不是一个好事情
def FinallyTest():
    print('I am starting------')
    while True:
        try:
            print('I am running!')
            raise IndexError('IndexError!')
        except NameError as e:
            print('NameError happened %s' % e)
        finally:
            print('finally executed!')
            break  # 第一个陷阱


FinallyTest()
# I am starting------
# I am running!
# finally executed!

'''
上面的例子中try代码块抛出了IndexError异常，但是在except块却没有对应的异常声明，按常理该异常会向上层抛出，可是程序输出却没有提示任何的
异常发生，也就是IndexError异常被丢失了。
这究竟是什么原因呢？当try块中发生异常的时候，如果在except语句中找不到对应的异常处理，异常将会被临时保存起来，当finally执行完毕的时候，
临时保存的异常会再次被抛出，但如果finally语句中产生了新的异常或者执行了return或者break语句，那么临时保存的异常将会被丢失，从而导致异常
屏蔽。
这是finally使用时候要小心的第一个陷阱。
'''


# 总返回一个不正确的值
def ReturnTest(a):
    try:
        if a <= 0:
            raise ValueError('Data can not be negative')
        else:
            return a
    except ValueError as e:
        print(e)
    finally:
        print('The end!')
        return -1  # 第2个陷阱


print(ReturnTest(0))
print(ReturnTest(2))
# Data can not be negative
# The end!
# -1
# The end!
# -1

'''
ReturnTest(2)返回是-1，是因为finally是必须执行的，但它return -1，故此结果也就-1，这是finally第二个陷阱
'''
