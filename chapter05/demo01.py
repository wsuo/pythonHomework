"""
@author: wsuo
@contact: wangsuoo@foxmail.com
@file: demo01.py
@time: 2020/3/25
"""
# 这个不是作业,是自己写的一个进度条程序
import time

total = 20
print("下载开始".center(total + 5, "="))
old = time.perf_counter()
for i in range(total + 1):
    # 打印字符,作为视图
    a = "*" * i
    b = "-" * (total - i)
    # 计算比例,执行了的百分比
    c = (i / total) * 100
    # 取差值作为执行时间
    new = time.perf_counter() - old
    # \r 是用来移动光标至开头处, 本来 end 是以 \n 结尾实现换行, 现在以空字符结尾代表啥也不干
    print("\r{2:<3.0f}%[{0:s}->{1:s}] {3:>3.2f}s".format(a, b, c, new), end="")
    time.sleep(0.2)
print('\n' + "下载完成".center(total + 5, "="))
