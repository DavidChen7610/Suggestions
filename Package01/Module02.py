# coding: utf-8
import sys

print(__name__, '\n')
print(sys.path, '\n')

from Module01 import Test  # noqa
print(sys.path)
