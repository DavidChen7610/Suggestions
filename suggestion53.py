# coding: utf-8
"""
建议53：用状态模式美化代码
抽取state模块的代码到项目来方便调试
"""
from state import switch, stateful, State, behavior


@stateful
class People(object):
    class Workday(State):
        default = True

        @behavior
        def day(self):
            print('work hard.')

    class Weekend(State):
        @behavior
        def day(self):
            print('play harder!')


people = People()
for x in range(2):
    for i in range(1, 8):
        if i == 6:
            switch(people, People.Weekend)
        if i == 1:
            switch(people, People.Workday)

        people.day()


# 当调用当前状态不存在的行为时，出错信息抛出的是AttributeError，从而避免把问题变为复杂的逻辑错误，让程序员更容易找到出错位置，进而修正问题
@stateful
class Player(object):
    class NeedSignin(State):
        default = True

        @behavior
        def signin(self, user, pwd):
            print('(%s, %s)singin' % (user, pwd))
            switch(self, Player.Signin)

    class Signin(State):
        @behavior
        def move(self, dst):
            print('move to %s' % dst)

        @behavior
        def atk(self, other):
            print('atk %s' % other)


p = Player()
# p.signin('user', 'pwd')
p.move(3)
p.atk('pc')
