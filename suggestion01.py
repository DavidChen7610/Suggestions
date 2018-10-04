#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yanghua'


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
    print('{greet} from {language}.'.format(greet='Hello world', language='Python'))

    # str.format()方法非常清晰的表明了这条语句的意图，而且模板的使用也减少了许多不必要的字符，使可读性得到了很大的提升，
    # Pythonnic的库或者框架
    # 一个Pythonic的库或者框架能更加容易的，更加自然的完成任务，如果用Python编写的库或框架迫使程序员编写累赘的或者不推荐的代码
    # 那么可以肯定的说它是不Pythonic的，现在业内通常认为Flask是比较Pythonic的。

    # 示例代码如下
    # from flask import Flask
    # app = Flask(__name__)
    #
    # @app.route("/")
    # def hello():
    #     return "Hello World!"
    #
    # if __name__ == "__main__":
    #     app.run()

    # 一个Pythonic的框架不会对已经通过惯用法完成的东西重复发明轮子，而且它遵循常用的Python惯例，创建Pythonic的框架极其困难，什么理念
    # 更酷，更符合语言习惯对此毫无帮助，事实上这些年来优秀的Python代码的特性也再不断的演化，比如现在认为generator之类的特性都是比较
    # Pythonic的

    # 包和模块结构日益规范化，现在的库和框架跟随了以下的潮流：
    # 包和模块的命名采用小写，单数形式，而且短小
    # 包通常仅作为命名空间，如只包含空的__init__.py
