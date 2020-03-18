# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0018 16:25
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo08.py
# @Software: PyCharm
'''
重复元素判定。
编写一个函数，接受列表作为参数，
如果一个元素在列表中出现不止一次，则返回True，否则返回False。
但不要改变原来列表的值。
同时编写调用这个函数和测试结果的程序。
'''


def funct(lt):
    for i in lt:
        if (lt.count(i)) > 1:
            return False
    return True


n = input()
if not funct(list(n)):
    print("有重复元素")
else:
    print("无重复元素")
