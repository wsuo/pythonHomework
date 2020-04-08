"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo03.py
@time: 2020/4/8 0008
"""

# 已知有个列表[1,2,3,4,5]，让列表的每个元素加1，结果不能被2整除的元素筛选出来。
lt1 = [1, 2, 3, 4, 5]
# 使用列表推导式和 filter() 函数过滤
lt2 = list(filter(lambda x: x % 2 != 0, [i + 1 for i in lt1]))
print(lt2)
