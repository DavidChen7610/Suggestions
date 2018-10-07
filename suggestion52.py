# coding: utf-8
"""
建议52：用发布订阅模式实现松耦合
发布订阅模式是一种编程模式，消息的发送者不会发送信息给特定的接收者，而是将发布的消息分为不同的类别
直接发布，并不关注订阅者是谁；而订阅者可以对一个或多个类别感兴趣，且只接收感兴趣的消息，并不关注
是哪个发布者的消息。
发布订阅模式，双方不需要知道对方的存在。要实现这个模式需要一个中间代理人Broker，它维护着发布者和
订阅者的关系：订阅者把感兴趣的主题告诉它，而发布者的信息也通过它路由到各个订阅者处。
"""

# 最好将sub和pub存放在Broker模块中，这里图方便直接放这里用
from collections import defaultdict
route_table = defaultdict(list)


def sub(topic, callback):
    if callback in route_table[topic]:
        return
    route_table[topic].append(callback)


def pub(topic, *a, **kw):
    for func in route_table[topic]:
        func(*a, **kw)


def greeting(name):
    print('Hello, %s' % name)


sub('greet', greeting)
pub('greet', 'LaiYongHao')

# 相对于这个简化版本，blinker和python-message两个模块的实现要完备得多。
# blinker已经被用在多个项目上，如是flask和django，而python-message则支持更多丰富的特性
# message模块是laiyonghao自己写的，原来只能用在python2.x，我抽出来改写了__init__.py使其能应用在python3.5上

# 以下例子是用message解耦，满足不同日志输出
import message
LOG_MSG = ('log', 'foo')


def bar():
    """重要函数，给外部调用者使用，执行前先打印些信息，方便调试查看"""
    message.pub(LOG_MSG, 'Haha, Calling bar().')
    # do_sth()


# 以下代码是在别的文件调用
"""
## 使用者在console直接输出调试信息
import message
import suggestion52

def handle_foo_log_msg(txt):
    print(txt)

message.sub(suggestion52.LOG_MSG, handle_foo_log_msg)
suggestion52.bar()

## 使用者在logging中输出日志信息
import message
import suggestion52

def handle_foo_log_msg(txt):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(txt)

message.sub(suggestion52.LOG_MSG, handle_foo_log_msg)
suggestion52.bar()
"""

# 订阅发布模式是观察者模式的超集，它既不关注消息的发布者，也不关注消息的订阅者，它还可以退化成为
# 观察者模式，如下：
from message import observable


def greet(people):
    print('Hello, %s.' % people.name)


@observable
class Foo(object):
    def __init__(self, name):
        print('Foo')
        self.name = name
        self.sub('greet', greet)

    def pub_greet(self):
        self.pub('greet', self)


foo = Foo('lai')
foo.pub_greet()


# 除了简单的sub()/pub()之外，它还支持取消订阅(unsub())和中止消息传递
import message


def hello(name):
    print('hello %s' % name)
    ctx = message.Context()
    ctx.discontinued = True
    return ctx


def hi(name):
    print('you cann\'t see me')


message.sub('greet', hello)
message.sub('greet', hi)
message.pub('greet', 'lai')
