#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：使用lambda的要点是什么？
答：要点是要注意它只是一个表达式，适用于返回一个较小的内联函数对象。它可以通过默认参数的方法传递状态，而且是遵循LEGB作用域查找法则的。它们通常出现在GUI这样的基于回调的程序中，并且与map和filter这些期待一个处理函数的函数工具密切相关。
'''
