#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2021/7/23 9:02
# @File     : conftest.py
# @Project  : PytestApiTest

import pytest

from common.data_util import Data_Read_Write_util
from common.readconfig import ReadConfig
from serivice_define import auth_token


@pytest.fixture(scope='session',autouse=True)
def get_project_id():
    project_id = ReadConfig().get_userInfo("project_id")
    return project_id

@pytest.fixture(scope='session',autouse=True)
def get_token():
    token = auth_token.get_token()
    return token

@pytest.fixture(scope='session',autouse=True)
def setconf():

    # 清空extract.yaml文件
    Data_Read_Write_util(write_yaml_path='./../../extract.yaml').clear_yaml()
    yield
    print('clearing------------')

