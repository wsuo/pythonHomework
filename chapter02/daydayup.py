# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 0011 11:12
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : daybase.py
# @Software: PyCharm

'''
如果周一到周五努力,周末退步还想达到一直努力的水平
使用不断试错的方法,while循环遍历
'''
def function(step):
    base = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            base *= (1 - 0.01)
        else:
            base *= (1 + step)
    return base


step = 0.01
while function(step) < pow(1.01, 365):
    step += 0.001
print("周一到周五每天需要努力：{:.1f}%".format(step * 100))
