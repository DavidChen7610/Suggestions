# coding: utf-8
"""
建议39：使用Counter进行计数统计
"""

# 1使用dict
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = {}
for item in some_data:
    if item in count_frq:
        count_frq[item] += 1
    else:
        count_frq[item] = 1
print(count_frq)
# {'z': 1, 'a': 3, 4: 2, 5: 2, '2': 2, 'b': 1, 7: 1, 2: 1, 'd': 1}

# 2使用defaultdict
from collections import defaultdict
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = defaultdict(int)
for item in some_data:
    count_frq[item] += 1
print(count_frq)
# defaultdict(<class 'int'>, {2: 1, 4: 2, '2': 2, 7: 1, 'z': 1, 'a': 3, 'd': 1, 'b': 1, 5: 2})

# 3使用set和list
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_set = set(some_data)
count_list = []
for item in count_set:
    count_list.append((item, some_data.count(item)))
print(count_list)
# [(2, 1), ('2', 2), (4, 2), (5, 2), ('d', 1), (7, 1), ('z', 1), ('b', 1), ('a', 3)]

# 最pythonic方法
from collections import Counter
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
print(Counter(some_data))
# Counter({'a': 3, 4: 2, 5: 2, '2': 2, 'z': 1, 2: 1, 'b': 1, 7: 1, 'd': 1})
