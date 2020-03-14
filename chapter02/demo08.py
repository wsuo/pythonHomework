# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 0014 11:44
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo08.py
# @Software: PyCharm
str = input()

for i in str:
    num = ord(i)  # 得到ASCII码
    if (65 <= num <= 90):  # 如果是大写字母
        str = str.replace(i, chr(155 - num))

print(str)