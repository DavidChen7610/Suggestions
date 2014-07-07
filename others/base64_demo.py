# -*- coding: utf-8 -*-
__author__ = 'florije'

import base64

if __name__ == '__main__':
    based_str = base64.b64encode('fuboqing')
    print based_str
    print base64.b64decode(based_str)

    print base64.b64encode('')
    urlsafe_str = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
    print urlsafe_str
    print base64.urlsafe_b64decode('QUFodHRwOi8vd3d3LmJhaWR1LmNvbS9pbWcvc3NsbTFfbG9nby5naWZaWg==')