#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2021/8/3 9:10
# @File     : pytest_main.py
# @Project  : PytestApiTest
import time

import pytest
import os

if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir", "./temp", "--capture=sys"])
    os.system('allure generate ./temp -o ./report --clean')
    time.sleep(2)
    os.system("allure open -h 127.0.0.1 -p 8083 ./report")