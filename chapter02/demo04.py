# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 10:43
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo04.py
# @Software: PyCharm
import turtle as t


def draw():
    for i in range(3):
        t.fd(300)
        t.right(120)


draw()
t.penup()
t.fd(100)
t.left(60)
t.fd(100)
t.right(120)
t.pendown()
draw()
t.done()
