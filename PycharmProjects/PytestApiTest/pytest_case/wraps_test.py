#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2022/3/15 11:10
# @File     : wraps_test.py
# @Project  : PytestApiTest

from functools import wraps

def decorator_with_argument(argument = ''):

    def decorator_with_argument(argument=''):
        def outer(func):
            message = argument + func.__name__

            @wraps(func)
            def inner(*args, **kwargs):
                print(message)
                print('This is inner function running')
                return func(*args, **kwargs)
            return inner

        return outer