# -*- coding: utf-8 -*-
__author__ = 'florije'
import time


def reverse_str(str_arg):
    if len(str_arg) == 1:
        return str_arg
    else:
        return str_arg[-1] + reverse_str(str_arg[:-1])


if __name__ == '__main__':
    # s_arg = input('list:')
    # print s_arg
    # print type(s_arg)

    # for i in range(1, 20):
    # print '%02d' % i
    #
    # print "Age:%02d" % 1
    # title = ''
    # f =file("%s.html" % title, "a")

    u = u'汉'
    print repr(u)
    s = u.encode('UTF-8')
    print repr(s)
    u2 = s.decode('UTF-8')
    print u2
    print repr(u2)  # u'\u6c49'
    # 对unicode进行解码是错误的
    # s2 = u.decode('UTF-8')
    # 同样，对str进行编码也是错误的
    # u2 = s.encode('UTF-8')

    a = ['anhui:0', 'shtel1:0', 'shtel2:0', 'weinan3:0', 'weinan1:0', 'weinan2:0', 'luckyhost:100', 'crh:99']
    a.sort(key=lambda item: int(item.split(':')[1]))
    print a

    print reverse_str('fuboqing')

    t = time.clock()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print [item * 3 if tx.index(item) < 3 else item for item in tx]
    # tx[:3] = [i*3 for i in tx[:3]]
    # print tx

    def aa(a):
        a[0] = a[0] * 3
        a[1] = a[1] * 3
        a[2] = a[2] * 3
        return a

    print aa(a)
    print time.clock() - t