#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2021/8/4 8:53
# @File     : get_root_path.py
# @Project  : PytestApiTest
import os

def get_path():

    path = os.path.split(os.path.realpath(__file__))[0]
    return path
