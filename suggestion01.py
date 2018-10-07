# coding: utf-8
"""
建议1：理解Pythonic概念

在ipython中输入import this，显示《The Zen of Python》（Python之禅）

包和模块结构日益规范化，现在的库和框架跟随了以下的潮流：
包和模块的命名采用小写，单数形式，而且短小
包通常仅作为命名空间，如只包含空的__init__.py
"""


def quick_sort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for item in array:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 2]
    print(quick_sort(arr))

    a = [1, 2, 3, 4]
    print(a[::-1])
    print(list(reversed(a)))
    c = 'abcdefg'
    print(c[::-1])

    print('Hello %s!' % ('Tom', ))
    print('Hello %(name)s!' % {'name': 'Tom'})

    value = {'greet': 'Hello world', 'language': 'Python'}
    print('%(greet)s from %(language)s.' % value)

    # 占位符，来自于大家的先验知识，其实对于新手而言，有点莫名其妙，所以更具有Pythonic风格的代码其实是下面：
    # str.format()方法非常清晰的表明了这条语句的意图，而且模板的使用也减少了许多不必要的字符，使可读性得到了很大的提升，
    print('{greet} from {language}.'.format(greet='Hello world', language='Python'))
