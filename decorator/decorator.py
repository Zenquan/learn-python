# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     decorator
   Description :
   Author :       zenquan
   date：          2019/9/19
-------------------------------------------------
   Change Activity:
                   2019/9/19:
-------------------------------------------------
"""
__author__ = 'zenquan'

def hello(fnc):
    def s_hello():
        print('hello')
        fnc()

    return s_hello

@hello
def hi():
    print('hi')

hi()