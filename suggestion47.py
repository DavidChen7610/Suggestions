# coding: utf-8
"""
建议47：使用logging记录日志信息
logging lib包含以下4个主要对象：
1 logger
2 Handler
3 Formatter
4 Filter
logging.basicConfig([**kwargs])提供对日志系统的基本配置，默认使用StreamHandler和Formatter
并添加到root logger

尽量为logging取一个名字而不是采用默认，这样当在不同的模块使用的时候，其他模块只需要使用以下代码就可以
方便地使用同一个logger，因为它本质上符合单例模式
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
其他模块使用时，只需要from xxx import logger
logger.debug('xxx')
logger.info('xxx')

logging只是线程安全，不支持多进程写入同一个日志文件，因此对于多个进程，需要配置不同的日志文件。
"""

import traceback
import sys
import logging

gList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
logging.basicConfig(
    level=logging.DEBUG,
    filename='log.txt',
    filemode='w',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)

# 控制台console输出
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def f():
    gList[5]
    logging.info('[INFO]:calling method g() in f()')
    return g()


def g():
    logging.info('[INFO]:calling method h() in g()')
    return h()


def h():
    logging.info('[INFO]:Delete element in gList in h()')
    del gList[2]
    logging.info('[INFO]:calling method i() in h()')
    return i()


def i():
    logging.info('[INFO]:Append element i to gList in i()')
    gList.append('i')
    print(gList[7])


if __name__ == '__main__':
    logging.debug('Information during calling f():')
    try:
        f()
    except IndexError as ex:
        print('Sorry, Exception occured, you accessed an element out of range')
        # traceback.print_exec()
        ty, tv, tb = sys.exc_info()
        logging.error('[ERROR]:Sorry, Exception occured, you accessed an element out of range')
        logging.critical('object info:%s' % ex)
        logging.critical('Error Type:{0}, Error Information:{1}'.format(ty, tv))
        logging.critical(''.join(traceback.format_tb(tb)))
        sys.exit(1)
