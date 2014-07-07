# -*- coding: utf-8 -*-
__author__ = 'florije'

import base64

'''
In [1]: s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

In [2]: import struct

In [3]: struct.unpack('<ccIIIIIIHH', s)
Out[3]: ('B', 'M', 691256, 0, 54, 40, 640, 360, 1, 24)
'''

if __name__ == '__main__':
    based_str = base64.b64encode('fuboqing')
    print based_str
    print base64.b64decode(based_str)

    print base64.b64encode('')
    urlsafe_str = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
    print urlsafe_str
    print base64.urlsafe_b64decode('QUFodHRwOi8vd3d3LmJhaWR1LmNvbS9pbWcvc3NsbTFfbG9nby5naWZaWg==')