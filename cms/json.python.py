# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     json.python
   Description :
   Author :       zenquan
   date：          2019/9/19
-------------------------------------------------
   Change Activity:
                   2019/9/19:
-------------------------------------------------
"""
__author__ = 'zenquan'

import json
json_data = open('./package.json').read()

data = json.loads(json_data)

print(type(data))

for (key, val) in data.items():
    print(key, val)