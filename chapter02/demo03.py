# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 10:39
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo03.py
# @Software: PyCharm
import turtle as t


def draw():
    for i in range(4):
        t.pendown()
        t.fd(200)
        t.penup()
        t.fd(20)
        t.right(270)
        t.fd(20)
        t.pendown()


t.penup()
t.fd(20)
t.pendown()
draw()
t.done()
