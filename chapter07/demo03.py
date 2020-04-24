"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo03.py
@time: 2020/4/24 0024
"""
'''
打开一个英文文本文件，编写程序读取其内容，并把其中的大写字母变成小写字母，小写字母变成大写字母。
'''

txt = open("./b.txt", "r").read()
print(txt)
ls1 = ["".join(i.split()) for i in txt]
ls2 = []
for i in ls1:
    if i.isalpha():
        if i.isupper():
            ls2.append(i.lower())
        else:
            ls2.append(i.upper())
    elif i == '':
        ls2.append(" ")
    elif i == '\n':
        ls2.append("\n")
    else:
        ls2.append(i)
fl = open("./c.txt", "w")
fl.writelines(ls2)
print(ls1)
print(ls2)


