# coding: utf-8
"""
建议2：编写Pythonic代码

深入学习业界公认的比较Pythonic的代码，比如Flask，gevent和requests等

关于PEP8编程规范，最好在编辑器中使用相应的插件，统一代码风格。

## 额外补充

gevent对python3来说不算好，可以用asyncio
参看 http://www.dongwm.com/archives/使用Python进行并发编程-我为什么不喜欢Gevent/
参看 https://www.cnblogs.com/zhaof/p/7536569.html
使用Gevent的性能确实要比用传统的线程高，甚至高很多。但这里不得不说它的一个坑：
Monkey-patching，我们都叫猴子补丁，因为如果使用了这个补丁，Gevent直接修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading
和 select等模块，而变为协作式运行。但是我们无法保证你在复杂的生产环境中有哪些地方使用这些标准库会由于打了补丁而出现奇怪的问题
第三方库支持。得确保项目中用到其他用到的网络库也必须使用纯Python或者明确说明支持Gevent


requests 绝对可以代替标准库的urllib，提供更简单更人性化的库，Requests: HTTP for Humans
http://docs.python-requests.org/en/master/
"""

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
