#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2022/3/11 15:37
# @File     : test_fixtures1.py
# @Project  : PytestApiTest
import allure
import pytest
from common.ApiautoLogging import LoggerForApitest

LoggerForApitest.setlogger("test_case")



def setup_module(module):
    print("setup module=============")

def teardown_module(module):
    print("teardown module==========")

def setup_function(function):
    print("setup function===========")

def teardown_function(function):
    print("teardown function========")

def setup():
    print("setup====================")

def teardown():
    print("teardown=================")
@pytest.mark.run(order=3)
@allure.title("testcase1")
@allure.description("I am first test_case1")
@allure.feature("I am feature")
@allure.story('story_1')
@allure.severity("normal")
def test_case1():
    """
    testcase1
    :return:
    """
    LoggerForApitest.writeInfoLog("I AM CASE1")
    assert 1 == 1
@pytest.mark.run(order=2)
@allure.title("testcase2")
@allure.description("I am first test_case2")
@allure.story('story_2')
@allure.severity("blocker")
def test_case2():
    print('I am case2')
    LoggerForApitest.writeInfoLog("I AM CASE2")
    assert 3 == 3
@pytest.mark.run(order=1)
@allure.title("testcase3")
@allure.description("I am first test_case3")
@allure.story('story_3')
def test_case3():
    print('I am case3')
    LoggerForApitest.writeInfoLog("I AM CASE3")
    assert 3 == 3
