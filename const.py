# -*- coding: utf-8 -*-
__author__ = 'florije'


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError, "Can't change const.%s" % key
        if not key.isupper():
            raise self.ConstCaseError, "const key '%s' is not all uppercase" % key
        self.__dict__[key] = value


import sys

sys.modules[__name__] = _const()