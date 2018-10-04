# -*- coding: utf-8 -*-
__author__ = 'florije'
'''
[]/()/{}一致的容器初始化形式
'''

# 补充
# 文件句柄当做一个可迭代对象，可轻易读出文件内容
f = open('test.txt')
result = [i for i in f if 'abc' in i]  # 文件句柄可以当做可迭代对象
print(result)

# 列表解析更为直观清晰，代码更为简洁。
# 列表解析的效率更高。列表解析在时间上有一定的优势。但对于大数据处理，列表解析并不是一个最佳选择，过多的内存消耗可能会导致MemoryError
