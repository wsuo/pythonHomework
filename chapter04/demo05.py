# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0018 13:40
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo05.py
# @Software: PyCharm
# 随机密码生成。编写程序，在26个大、小写字母和10个数字组成的列表中随机生成1个密码，密码长度8位。
import random as r
lt = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)] + [chr(k) for k in range(48, 58)]
lts = []
for i in range(8):
    lts.append(r.choice(lt))
print(''.join(lts))
