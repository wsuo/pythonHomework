# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 12:16
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo04.py
# @Software: PyCharm
inp = input()
dist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in inp:
    if i in dist:
        index = dist.index(i)
        inp = inp.replace(i, dist[-index - 1])
print(inp)

# 解法二: ASCII码