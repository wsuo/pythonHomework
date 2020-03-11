# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 10:17
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo01.py
# @Software: PyCharm
import turtle as t


def draw():
    m = 0
    for i in range(40):
        m += 5
        t.fd(m)
        t.left(90)


draw()
t.done()
