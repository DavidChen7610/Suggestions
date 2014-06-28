# -*- coding: utf-8 -*-
#!/usr/bin/python
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
    print quick_sort(arr)

    a = [1, 2, 3, 4]
    print a[::-1]
    print list(reversed(a))
    c = 'abcdefg'
    print c[::-1]
