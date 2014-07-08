# -*- coding: utf-8 -*-
__author__ = 'florije'
from fabric.api import *

env.hosts = ['106.186.117.251:22']
env.user = "florije"
env.password = '***'


def hello():
    print("Hello fabric!")


'''
D:\Projects\python\suggestion_env\Scripts\fab-script.py
-f fabfile hello
D:\Projects\python\Suggestions\others
'''


def remote():
    '''远程文件拷贝操作'''
    run('pwd')
    run('cp /home/florije/tmp/text.txt /home/florije/tmp/xiaoqi.txt')
    print 'remote copy file success'