#! /usr/bin/python3
# -*- coding:utf8 -*-

﻿'''
问：当简单赋值语句出现在class语句顶层时，会发生什么？
答：当简单赋值语句(X=Y)出现在类语句的顶层时，就会把数据属性附加在这个类上(class.X)。就像所有的类属性，这会由所有的实例共享。不过，数据属性并不是可调用的方法函数。
'''