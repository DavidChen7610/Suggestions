# coding: utf-8
"""
理解python与C语言的不同之处

1 缩进和{}
2 ' 与 "
3 三元操作符 C?X:Y 和 X if C else Y
4 switch...case 和 字典
"""


def f(num):
    return {
        0: "The first one!",  # noqa
        1: "The second one!",
        2: "The third one!"
    }.get(num, "No vainly!")


if __name__ == '__main__':
    print(f(2))
