# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0018 12:27
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo04.py
# @Software: PyCharm
lt1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
lt2 = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '2', '1']
n = input()
if len(n) == 18 and lt2[sum([int(n[i]) * lt1[i] for i in range(17)]) % 11] == n[-1]:
    print("{:s}是合法身份证号".format(n))
else:
    print("这不是合法身份证号")