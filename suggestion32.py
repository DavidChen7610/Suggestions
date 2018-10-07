# coding: utf-8
"""
建议32：警惕默认参数潜在的问题

参考建议29
"""


# 不正确的写法
def appendtest(newitem, lista=[]):
    print(id(lista))
    lista.append(newitem)
    print(id(lista))
    return lista


# 正确的写法
def appendtest(newitem, lista=None):
    if not lista:
        lista = []
    print(id(lista))
    lista.append(newitem)
    print(id(lista))
    return lista
