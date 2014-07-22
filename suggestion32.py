# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
警惕默认参数潜在的问题
'''

'''
默认参数可以给函数的使用带来很大的灵活性，当函数调用没有指定与形参对应的实参时就会自动使用默认参数。
'''

def appendtest(newitem, lista=[]):
    print id(lista)
    lista.append(newitem)
    print id(lista)
    return lista

'''
def appendtest(newitem, lista=None):
    if not lista: lista = []
    print id(lista)
    lista.append(newitem)
    print id(lista)
    return lista
'''


print appendtest('a', ['b', 2, 4, [1, 2]])

'''
现在思考一下，如果第二个参数采用默认参数，连续调用两次appendtest(1), appendtest('a'),函数的返回值应该是多少呢？
'''