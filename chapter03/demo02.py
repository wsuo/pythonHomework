# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 11:57
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo02.py
# @Software: PyCharm
num = input()
a = int(num[0])
n = eval(num[2])
sum = 0;
for i in range(n):
    var = 1
    for j in range(i + 1):
        var *= a
    sum += var

print("s = " + str(sum))
