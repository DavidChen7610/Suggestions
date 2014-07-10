# -*- coding: utf-8 -*-
__author__ = 'florije'


def quick_sort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    print quick_sort([9,8,4,5,32,64,2,1,0,10,19,27])