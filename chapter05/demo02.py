"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo02.py
@time: 2020/4/8 0008
"""
# 利用filter()函数过滤出1-100中平方根是整数的数。输出结果第一行显示这些数，第二行打印出这些数的总个数。
# 使用高阶函数 filter():
#   第一个参数传递 匿名函数用来处理 第二个列表参数的值,完成过滤操作
#   第二个参数传递 一个列表推导式, 也就是一个列表,值为[1~100]
lt = list(filter(lambda x: pow(x, 0.5).is_integer(), [i for i in range(1, 101)]))
# 输出函数,sep 代表中间字符间以什么分割,查看源码得知
print(lt, len(lt), sep='\n')
