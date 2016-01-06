#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
为什么回调一个超类的方法来运行默认操作而不是在子类中复制和修改其代码要更好？

答：复制和修改代码会使得维护时工作量增大，而且复制代码可能导致代码冗余。如果可以利用回调超类的方法实现时就应当避免在子类中复制和修改代码。
"""