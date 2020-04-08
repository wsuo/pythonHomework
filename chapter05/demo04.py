"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo04.py
@time: 2020/4/8 0008
"""


# 实现multi()函数，参数个数不限，返回所有参数的乘积，调用并运行该函数。
# 参数个数不限可以使用 * 占位符,然后循环遍历相乘即可
def multi(*a):
    total = 1
    for i in a:
        total *= i
    return total


print(multi(1, 2, 3, 4, 5))
