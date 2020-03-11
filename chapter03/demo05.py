# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 12:46
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo05.py
# @Software: PyCharm
# 也就是说有效的增长的天数为 365/7 * 4 天
day = int(365 // 7 * 4)


def function():
    base = 1
    for i in range(day):
        base *= (1 + 0.01)
    return base


print("连续学习365天后能力值是: {:.2f}".format(function()))
