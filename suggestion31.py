# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
记住函数传参既不是传值也不是传引用
'''

'''
Python 中的函数参数到底是传值还是传引用呢，这比较纠结，很多的论坛也有这样的讨论，总结来说基本有3个观点，传引用，传值，可变对象传引用，
不可变对象传值
那到底是怎么进行处理呢？
1、传引用
'''


def inc(n):
    print id(n)
    n = n + 1
    print id(n)

n = 3
print id(n)
inc(n)
print n

'''
7185088
7185088
7185076
3
'''
'''
按照传引用的概念，上面的例子期望的输出应该是4，并且inc()函数里面执行操作n=n+1的前后的id值应该是不变的，
可是结果的确实，n的值还是没有变化，但是id(n)的值在函数体前后却不一致了。看来传引用这个不是很正确了。
'''


def change_list(orginator_list):
    print 'orginator list is:', orginator_list
    new_list = orginator_list
    new_list.append('I am new!')
    print 'New list is:', new_list
    return new_list


orginator_list = ['a', 'b', 'c']
new_list = change_list(orginator_list)
print new_list
print orginator_list

'''
传值通俗的来讲就是这个意思，你在内存中有一个位置，我也有一个位置，我把我的值复制给你，以后你做什么就跟我没有关系啦，我是我，你是你，
但是这上面的就不是这么回事了，看来纯碎的说传值也是不对的
'''

'''
可变对象传引用，不可变对象传值，这个说法最靠谱，好多人也是这么理解的，但是这个说法到底对不对？我们看一个例子的说：
'''


def change_me(org_list):
    print id(org_list)
    new_list = org_list
    print id(new_list)
    if len(new_list) > 5:
        new_list = ['a', 'b', 'c']
    for i, e in enumerate(new_list):
        if isinstance(e, list):
            new_list[i] = '***'
    print new_list
    print id(new_list)


test1 = [1, ['a', 1, 3], [2, 1], 6]
change_me(test1)
print test1
test2 = [1, 2, 3, 4, 5, 6, [1]]
change_me(test2)
print test2

if __name__ == '__main__':
    pass