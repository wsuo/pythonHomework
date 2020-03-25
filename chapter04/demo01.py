# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 0016 18:26
# @Author  : 王硕
# @Email   : ws2821@yeah.net
# @File    : demo01.py
# @Software: PyCharm
"""
一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：

首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；

然后将计算的和对11取模得到值Z；最后按照以下关系对应Z值与校验码M的值：

Z：0 1 2 3 4 5 6 7 8 9 10

M：1 0 X 9 8 7 6 5 4 3 2

1、先把集合反转了:
10 9 8 7 6 5 4 3 2 1 0
2、然后加2:
12 11 10 9 8 7 6 5 4 3 2
3、从 9 往后是一样的，再将前三个变为12,11,10
得到的集合即为结果


输入一个身份证号码，请你验证校验码的有效性，给出结论是否为合法身份证号码

输入样例：

320124198808240056

输出样例：

320124198808240056是合法身份证号
"""


# 运算函数
def decide(mm):
    # sum = 0
    # 在这里定义的原因是考虑到如果程序都运行不到这一步会浪费空间
    lt = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # for i in range(17):
    # 对前17位数字加权求和
    # tmp = int(m[i]) * int(lt[i])
    # sum += tmp
    # 使用列表推导式更为简单
    mod = sum([int(mm[i]) * int(lt[i]) for i in range(17)]) % 11
    # 取模判断
    nav = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rev = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    # if [i for i in nav if mod == nav[i]][0]
    for j in nav:
        if mod == nav[j]:
            return rev[j]
    return


# 判断函数
def doit(men, flag1):
    if flag1:
        print("{:s}是合法身份证号".format(men))
    else:
        print("{:s}不是合法身份证号".format(men))


# 主函数
m = input("请输入身份证号:")
# 首先判断长度是不是18位
totalFlag = False
if len(m) == 18:
    # 遍历一下看看是不是都是数字
    flag = True
    for i in range(17):
        if not m[i].isdigit():
            flag = False
    if flag:
        # 如果过了这两关，往下走判断
        tail = decide(m)
        if tail == int(m[-1]):
            totalFlag = True
doit(m, totalFlag)
#     else:
#         totalFlag = False
# else:
#     totalFlag = False

# print("请输入正确的身份证号!(不全是数字)")
# print("请输入正确的身份证号!(长度不对)")
