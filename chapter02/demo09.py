# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 0014 14:13
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo09.py
# @Software: PyCharm
str = input()
newStr = ''
for i in str:
    num = ord(i)  # 得到ASCII码
    if (65 <= num <= 90):  # 如果是大写字母
        i = i.replace(i, chr(155 - num))
    newStr += i  # 拼接到新字符串上

print(newStr)
