# coding=utf-8
__author__ = '胖'

import os


print os.path.isdir(r'c:\windows')
print os.path.isfile(r'c:\window\system32\notepad.exe')


try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python': 2.7})

from __future__ import division
