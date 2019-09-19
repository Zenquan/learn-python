# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     csv.python
   Description :
   Author :       zenquan
   date：          2019/9/19
-------------------------------------------------
   Change Activity:
                   2019/9/19:
-------------------------------------------------
"""
__author__ = 'zenquan'

import csv

csvfile = open('./data.csv', 'r')
# reader = csv.reader(csvfile)
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)