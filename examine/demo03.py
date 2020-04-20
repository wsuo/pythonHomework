"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo03.py
@time: 2020/4/20 0020
"""
import random
# 考虑到 % 效率低,使用位运算符
ls = list(filter(lambda x: x & 1 == 1, [random.randint(11, 99) for i in range(10)]))
print(ls)
