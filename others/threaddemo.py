# -*- coding: utf-8 -*-
__author__ = 'florije'

# import time
# import urllib2
#
#
# def get_responses():
#     urls = [
#         'http://www.baidu.com',
#         'http://www.taobao.com',
#         'http://www.dangdang.com',
#         'http://www.jd.com',
#         'http://www.126.com'
#     ]
#     start = time.time()
#     for url in urls:
#         print url
#         resp = urllib2.urlopen(url)
#         print resp.getcode()
#     print "Elapsed time: %s" % (time.time() - start)
# get_responses()

import urllib2
import time
from threading import Thread

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

def get_responses():
    urls = [
        'http://www.baidu.com',
        'http://www.taobao.com',
        'http://www.dangdang.com',
        'http://www.jd.com',
        'http://www.126.com'
    ]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time()-start)

get_responses()