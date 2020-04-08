"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo06.py
@time: 2020/4/8 0008
"""
# 利用map()函数，将两个列表对应相同位置的数据进行相加。
lt1 = [1, 2, 3, 4]
lt2 = [5, 6, 7, 8]
# 先打包成元组,然后相加
mp = map(lambda x: x[0] + x[1], zip(lt1, lt2))
print(list(mp))

# 看一下 zip 函数的输出结果
# print(list(zip(lt1, lt2)))
# [(1, 5), (2, 6), (3, 7), (4, 8)]
