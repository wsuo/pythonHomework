# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 0016 20:18
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo02.py
# @Software: PyCharm
'''
随机密码生成。编写程序，在26个大、小写字母和10个数字组成的列表中随机生成1个密码，密码长度8位。
'''

import random as r

n = eval(input("请输入生成密码的位数:"))
ch = ''
for i in range(n):
    up = r.randint(65, 90)
    low = r.randint(97, 122)
    dic = r.randint(48, 57)
    tmp = r.randint(1, 3)
    if tmp == 1:
        ch += chr(up)
    elif tmp == 2:
        ch += chr(low)
    else:
        ch += chr(dic)
# .append([chr(j) for j in range(97, 122)], [(chr(k)) for k in range(48, 57)])
