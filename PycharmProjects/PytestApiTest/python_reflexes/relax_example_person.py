#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : leimingming_wx405299
# @Time     : 2022/3/4 9:59
# @File     : relax_example_person.py
# @Project  : PytestApiTest

'''
python relax:
hasattr(查询对象中是否包含变量或方法)
getattr(获取对象中变量或函数的地址)
setattr(添加方法或变量到对象中)
delattr（删除对象中的变量，不能删除方法）
'''

def abc(self):
    print("%s is sleeping" %self.name)

class Person(object):

    def __init__(self,name):
        '''

        :param name:
        '''
        self.name = name

    def task(self):
        '''

        :return:
        '''
        print("%s正在交谈" %self.name)

if __name__ == '__main__':
    # 判断对象中是否有这个方法或变量
    person1 = Person("zhang san")
    person1.task()
    print(hasattr(person1,'task'))
    print(hasattr(person1,'name'))
    print(hasattr(person1,'123'))

    # 获取对象中的方法或变量的内存地址
    person2 = Person("Li si")
    n = getattr(person2,"name")
    print(n)
    t = getattr(person2,"task")
    print(t)
    s = getattr(person2,"abc","not found")
    print(s)

    # 为对象添加变量或方法
    person3 = Person("wang wu")
    setattr(person3,"age",30)
    print(person3.age)
    setattr(person3,"sleep",abc)
    print(person3.sleep(person3))

    # 删除对象中的变量。注意：不能用于删除方法
    p = Person("Lao da")
    delattr(p,"name")
    print(p.name)