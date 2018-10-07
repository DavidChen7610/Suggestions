# coding: utf-8
"""
建议37：按需选择sort()或者sorted()

python3只留下sorted()函数
sorted(iterable, key=None, reverse=False)
"""
"""
itemgetter(item, ...) --> itemgetter object

Return a callable object that fetches the given item(s) from its operand.
After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

"""

# 对字典进行排序
from operator import itemgetter

# 根据value来排序
phonebook = {'Linda': '7750', 'Bob': '9345', 'Carol': '5834'}
sorted_pb = sorted(phonebook.items(), key=itemgetter(1))
print(sorted_pb)
# [('Carol', '5834'), ('Linda', '7750'), ('Bob', '9345')]

# value是个列表，按列表的第2项来排序
mydict = {'Li': ['M', 7], 'Zhang': ['E', 2], 'Wang': ['P', 3], 'Du': ['C', 2], 'Ma': ['C', 9], 'Zhe': ['H', 7]}
sorted_pb = sorted(mydict.items(), key=lambda x: itemgetter(1)(x[1]))  # lambda语法在python3有所改变，不支持(k, v)，只允许一个参数表示元组
print(sorted_pb)
# [('Du', ['C', 2]), ('Zhang', ['E', 2]), ('Wang', ['P', 3]), ('Zhe', ['H', 7]), ('Li', ['M', 7]), ('Ma', ['C', 9])]

# 按字典中的'rating'和'name'来排序
gameresult = [{
    'name': 'Bob',
    'wins': 10,
    'losses': 3,
    'rating': 75.00
}, {
    'name': 'David',
    'wins': 3,
    'losses': 5,
    'rating': 57.00
}, {
    'name': 'Carol',
    'wins': 4,
    'losses': 5,
    'rating': 57.00
}, {
    'name': 'Patty',
    'wins': 9,
    'losses': 3,
    'rating': 71.48
}]
# sorted_pb = sorted(gameresult, key=lambda x: (x['rating'], x['name']))
sorted_pb = sorted(gameresult, key=itemgetter('rating', 'name'))  # 简化了lambda匿名函数
print(sorted_pb)
# [{'wins': 4, 'rating': 57.0, 'name': 'Carol', 'losses': 5}, {'wins': 3, 'rating': 57.0, 'name': 'David', 'losses': 5}, {'wins': 9, 'rating': 71.48, 'name': 'Patty', 'losses': 3}, {'wins': 10, 'rating': 75.0, 'name': 'Bob', 'losses': 3}]
