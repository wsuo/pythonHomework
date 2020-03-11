# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 11:42
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo01.py
# @Software: PyCharm
'''
# 解法一
num = input()
flag = True
size = len(num)
for i in range(size // 2):
    if num[i] != num[size - i - 1]:
        flag = False

if (flag == True):
    print(num + "是回文数")
else:
    print(num + "不是回文数")
'''
# 解法二
num = input()
if num == num[::-1]:
    print(num + "是回文数")
else:
    print(num + "不是回文数")