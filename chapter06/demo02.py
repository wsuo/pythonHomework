"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo02.py
@time: 2020/4/18 0018
"""
"""
@w1
def f():
    print("程序开始执行")
    for i in range(10):
        time.sleep(0.5)
    print("程序执行结束")
f()

有如上的功能函数f和f函数调用，写一个装饰器函数w1,
可以在f函数执行后打印输出f函数执行的时长是多少秒，小数点保留1位。运行结果如下所示：


程序开始执行
程序执行结束
程序执行了5.0秒
"""
import time


def w1(func):
    def fun():
        old = time.perf_counter()
        func()
        print("程序执行了{:.1f}秒".format(time.perf_counter() - old))

    return fun


@w1
def f():
    print("程序开始执行")
    for i in range(10):
        time.sleep(0.5)
    print("程序执行结束")


f()
