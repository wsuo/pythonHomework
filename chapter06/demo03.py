"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo03.py
@time: 2020/4/18 0018
"""
"""
@w1('张三')
def f(x):
    print("程序开始执行")
    for i in range(x):
        time.sleep(0.5)
    print("程序执行结束")
f(15)

有如上所示的功能函数f和f函数的调用，请完成装饰器函数w1的编写，可以使得函数f(15)执行后，得到如下的输出结果：


程序开始执行
程序执行结束
经过张三测试，程序执行了7.5秒
"""
import time


def w1(name):
    def w2(func):
        def fun(*args, **kwargs):
            old = time.perf_counter()
            func(*args, **kwargs)
            print("经过{}测试,程序执行了{:.1f}秒".format(name, time.perf_counter() - old))
        return fun
    return w2


@w1('张三')
def f(x):
    print("程序开始执行")
    for i in range(x):
        time.sleep(0.5)
    print("程序执行结束")


f(15)
