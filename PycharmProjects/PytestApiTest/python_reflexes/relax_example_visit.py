#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2022/3/7 10:08
# @File     : relax_example_visit.py
# @Project  : PytestApiTest

import relax_example_commons

def run():
    inp = input("请输入您想访问页面的url:  "+"\n").strip()
    if inp == "login":
        relax_example_commons.login()
    elif inp == "home":
        relax_example_commons.home()
    elif inp == "logout":
        relax_example_commons.logout()
    else:
        print("输入错误")

def run_relax():
    inp = input("请输入您想访问页面的url:  "+"\n").strip()
    if hasattr(relax_example_commons,inp):
        func = getattr(relax_example_commons,inp)
        func()
    else:
        print("输入错误")

def run_import():
    inp = input("请输入您想访问页面的url:  " + "\n").strip()
    (modules, func) = inp.split('/')
    obj = __import__(modules)
    if hasattr(obj,func):
        func = getattr(obj,func)
        func()
    else:
        print("输入错误")

def run_test_import(modules,func):
    obj = __import__(modules)
    print(obj)
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("func  is not in modules")

if __name__ == '__main__':
    #run
    #run_relax()
    #run_import()
    run_test_import("common.data_util", "talk")