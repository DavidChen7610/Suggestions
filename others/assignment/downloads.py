# -*- coding: utf-8 -*-
__author__ = 'florije'

import urllib
import os
from progressbar import *


def schedule(a, b, c):
    '''''
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
    '''
    w = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')), ' ',
         ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=w, maxval=100).start()

    # per = 100.0 * a * b / c
    # if per > 100:
    #     per = 100
    # print '%.2f%%' % per

    per = 100.0 * a * b / c
    if per < 100:
        pbar.update(int(per))
    else:
        pbar.update(int(per))
        pbar.finish()


url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
local = 'Python-2.7.5.tar.bz2'  # os.path.join('/data/software', 'Python-2.7.5.tar.bz2')
urllib.urlretrieve(url, filename=local, reporthook=schedule)