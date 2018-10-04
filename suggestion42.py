# import os

# 创建大文件的技巧
# f = open('large.csv', 'wb')
# f.seek(1024**3-1)
# f.write(b'\0')
# f.close()

# print(os.stat('large.csv').st_size)

"""
Pandas中处理csv文件的函数主要为read_csv()和to_csv()这两个，其中read_csv()读取csv文件的内容并返回DataFrame，to_csv()则是其逆过程。
"""

import pandas as pd
import csv


df = pd.read_csv('SampleData.csv', nrows=5, usecols=['OrderData', 'Item', 'Total'])
print(df)

dia = csv.excel()
dia.delimiter = '|'
print(pd.read_csv('SD.csv'))

# 设置csv文件与excel兼容，其中分隔符为'|'，而error_bad_lines=False会直接忽略不符合要求的记录
# 测试文件只有多余的'|'行才会被忽略，而少的'|'不会忽略
print(pd.read_csv('SD.csv', dialect=dia, error_bad_lines=False))

# 对文件分块处理并返回一个可迭代的对象
reader = pd.read_table('SampleData.csv', chunksize=3, iterator=True)
print(type(reader))
# <class 'pandas.io.parsers.TextFileReader'>
next(iter(reader))
