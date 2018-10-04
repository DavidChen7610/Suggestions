# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'yanghua'

# (1)避免劣化代码，主要有以下几个方面
# 避免只用大小写来区分不同的对象，
# 避免使用容易引起混淆的名称
# 不要害怕过长的变量名
# (2)深入认识Python有助于编写Pythonic代码
# 全面掌握Python提供给我们的所有特性，包括语言特性和库特性，其中最好的学习方式应该是通读官方手册中得Language Reference，掌握了语言特性
# 和库特性，以后许多惯用法就自然而然的掌握了，写代码时候自然会使用常见的公认的简短的惯用法来实现预期的效果，也使得代码显得尤为Pythonic
# 随着Python版本的更新，时间的推移，Python语言不断进化，社区不断成长，还需要学习每个Python版本提供的新特性，以及掌握他们的变化趋势，
# 从另一个角度看，一方面Python推荐使用大量的惯用法来完成任务，完成任务的唯一方法，另一方面，社区不断演变的新惯用法反过来又影响了语言的进化，
# 以更好的支持惯用法，
# 深入学习业界公认的比较Pythonic的代码，比如Flask，gevent和requests等
#


# ## 补充

# gevent对python3来说不算好，可以用asyncio
# 参看 https://link.zhihu.com/?target=http%3A//www.dongwm.com/archives/%25E4%25BD%25BF%25E7%2594%25A8Python%25E8%25BF%259B%25E8%25A1%258C%25E5%25B9%25B6%25E5%258F%2591%25E7%25BC%2596%25E7%25A8%258B-%25E6%2588%2591%25E4%25B8%25BA%25E4%25BB%2580%25E4%25B9%2588%25E4%25B8%258D%25E5%2596%259C%25E6%25AC%25A2Gevent/
# 参看 https://www.cnblogs.com/zhaof/p/7536569.html
# 使用Gevent的性能确实要比用传统的线程高，甚至高很多。但这里不得不说它的一个坑：
#   Monkey-patching，我们都叫猴子补丁，因为如果使用了这个补丁，Gevent直接修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行。但是我们无法保证你在复杂的生产环境中有哪些地方使用这些标准库会由于打了补丁而出现奇怪的问题
#   第三方库支持。得确保项目中用到其他用到的网络库也必须使用纯Python或者明确说明支持Gevent


# requests 绝对可以代替标准库的urllib，提供更简单更人性化的库，Requests: HTTP for Humans
# http://docs.python-requests.org/en/master/

import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
# 403
print(r.headers['content-type'])
# 'application/json; charset=utf8'
print(r.encoding)
# 'utf-8'
print(r.text)
# {"message":"Maximum number of login attempts exceeded. Please try again later.","documentation_url":"https://developer.github.com/v3"}
print(r.json())
# {'documentation_url': 'https://developer.github.com/v3', 'message': 'Maximum number of login attempts exceeded. Please try again later.'}
