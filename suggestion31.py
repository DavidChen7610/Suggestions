# coding: utf-8
"""
建议31:记住函数传参既不是传值也不是传引用

1、所有对象皆有id值。
2、所有名称只是对象的标签，单纯的标签没有意义，并没有指向内存，标签可以从对象上绑定，或者撕下。
3、所谓函数传参，只是标签的名称不一样，实际上它们的指向是相同对象。

给对象的赋值就是另外开辟新空间，标签名随之指新对象
n = 1
n = n + 1
两个n的id值不相同

a = [1]
a = a + [2]
两个a的id值也不相同

b = 3
c = b
b和c的id值相同

# 补充
foo(*args, **kwargs)中的args, kwargs是浅复制实参，参考建议33
"""


def inc(n):
    print(id(n))
    n = n + 1
    print(id(n))


n = 3
print(id(n))
inc(n)
print(n, '\n')


def change_list(orginator_list):
    print('orginator list is:', orginator_list)
    new_list = orginator_list
    new_list.append('I am new!')
    print('New list is:', new_list)
    return new_list


orginator_list = ['a', 'b', 'c']
new_list = change_list(orginator_list)
print(new_list)
print(orginator_list, '\n')


def change_me(org_list):
    print(id(org_list))
    new_list = org_list
    print(id(new_list))
    if len(new_list) > 5:
        new_list = ['a', 'b', 'c']
    for i, e in enumerate(new_list):
        if isinstance(e, list):
            new_list[i] = '***'
    print(new_list)
    print(id(new_list))


test1 = [1, ['a', 1, 3], [2, 1], 6]
change_me(test1)
print(test1, '\n')

test2 = [1, 2, 3, 4, 5, 6, [1]]
change_me(test2)
print(test2)
