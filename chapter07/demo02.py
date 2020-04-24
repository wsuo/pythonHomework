"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo02.py
@time: 2020/4/24 0024
"""
'''
读取一个文件，显示除了以井号（#）开头的行以外的所有行。
'''
ls = open("./a.txt", "r", encoding="utf-8").readlines()
[print(i, end="") for i in filter(lambda x: not x[0] == '#', ls)]


