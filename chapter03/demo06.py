# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 0014 10:58
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo06.py
# @Software: PyCharm

str = input()


def replace(str):
    for i in str:
        num = ord(i)  # 得到ASCII码
        if (num >= 65 & num <= 90):  # 如果是大写字母
            i = chr(155 - num)
    return str


replace(str)
print(str)
