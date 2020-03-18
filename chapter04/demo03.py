# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 0017 22:35
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo03.py
# @Software: PyCharm
lt1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
lt2 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
n = input()
if len(n) == 18 and lt2[sum([int(n[i]) * int(lt1[i]) for i in range(17)]) % 11] == int(n[-1]):
    print("{:s}是合法身份证号".format(n))
else:
    print("这不是合法身份证号")
