"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo05.py
@time: 2020/4/8 0008
"""


# 实现isPrime()函数，参数为整数，要有异常处理。如果整数是质数，返回True，否则返回False。调用并运行该函数。
def isPrime(a):
    try:
        for i in range(2, int(pow(a, 0.5) + 1)):
            if a % i == 0:
                return False
            else:
                return True
        return True
    # 捕捉类型异常,比如如果输入字符 'a' ,就会报此类型的错误
    except TypeError:
        print("输入不是整数")


print(isPrime(8))
