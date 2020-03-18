# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0018 13:46
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo06.py
# @Software: PyCharm
'''
对于给定的正整数N，求它的位数及其各位数字之和。
输入格式：
输入在一行中给出正整数N。
输出格式：
在一行中输出N的位数及其各位数字之和，中间用一个空格隔开。
输入样例：
321
输出样例：
3 6
'''
n = input()
print("{0:d} {1:d}".format(len(n), sum([int(i) for i in list(n)])))