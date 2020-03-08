# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 18:23
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo3.py
# @Software: PyCharm
'''
在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
a b c
01234
'''
'''
解法一:
num = input("请输入3个值并用空格隔开:")
a = eval(num[0])
b = eval(num[2])
c = eval(num[4])
print("结果为:%d" %(b * b - 4 * a * c))
'''


#解法二
num = input("请输入3个值并用空格隔开:")
print("结果为:%d" %(eval(num[2]) * eval(num[2]) - 4 * eval(num[0]) * eval(num[4])))
