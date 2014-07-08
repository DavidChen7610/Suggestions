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