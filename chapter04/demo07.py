# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0018 15:47
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo07.py
# @Software: PyCharm
"""
本题要求统计给定整数M和N区间内素数的个数并对它们求和。
输入格式:
输入在一行中给出两个正整数M和N（1≤M≤N≤500）。
输出格式:
在一行中顺序输出M和N区间内素数的个数以及它们的和，数字间以空格分隔。
输入样例:
10 31
输出样例:
7 143
"""
# lt = [i for i in range(int(m), int(n) + 1) for j in range(2, i) if i % j != 0]
# lt = [i for i in range(int(m), int(n) + 1) for j in range(1, i) if int(i) / int(j) == 0 and i != j and int(i) != 1]

m, n = input().split()
lt = []
for i in range(int(m), int(n) + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        lt.append(i)
print('{0:d} {1:d}'.format(len(lt), sum(lt)))

# flag = False
# if i % j == 0
# print(type(lt[1]))
# print(lt)
