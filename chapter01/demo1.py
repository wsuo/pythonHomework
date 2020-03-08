# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 0003 17:44
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo1.py
# @Software: PyCharm

'''
问题描述:

程序接收用户输入字符串，格式如下：

M OP N

其中M,N是数字，OP是 + - * / 其中一种操作符，根据OP输出运算结果，小数点保留两位。

注意：M和OP，OP和N之间可以有多个空格，不考虑输入错误的情况。
'''

#print("运算结果为:{:.2f}".format(eval(input("请输入:"))))
print("运算结果为:%.2f"%eval(input("请输入:")))