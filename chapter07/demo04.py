"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo04.py
@time: 2020/4/27 0027
"""

# print(table)
# 最后增加一列，名称为 '排名'
# l2 = []
# for i in table:
#     if i[0] == '姓名':
#         i.append('排名')
#         l2.append(i)
#     else:
#         l2.append(i)

import json

# f1 负责读入文件, f2 负责写入文件 + 代表同时具备读写功能
f1 = open('./a.csv', 'r+', encoding='utf-8')
f2 = open('./a.json', 'w+', encoding='utf-8')

# 使用列表推导式, 获取二维结构
table = [i.strip('\n').split(',') for i in f1.readlines()]

# 表头增加排名,然后我们就不需要表头了,因为它没法排序
table[0].append('排名')

# 由于 sort 函数和 extend 函数都是没有返回值的
# 所以我们必须事先存储待处理变量，如果题目中没给总分可以 sum([int(j) for j in x[1:]])
sortList = table[1:]
sortList.sort(key=lambda x: x[-1], reverse=True)

# 增加排名数字
for i in range(len(sortList)):
    sortList[i].append(str(i + 1))

# 表头加上已经排好序的表体
listHead = table[:1]
listHead.extend(sortList)

# 得到 Python 数据类型的 listHead
# 现在转化成 json 数据类型
# 1.首先建立映射关系,zip() 函数返回的是 zip 类型
#   我们要把 zip 类型转化成 字典类型;
toJson = []
for i in listHead[1:]:
    toJson.append(dict(zip(listHead[0], i)))

# 2.写入文件, dump 直接写入文件, dumps 返回 json 数据
json.dump(toJson, f2, ensure_ascii=False, indent=4)

# 释放资源
f1.close()
f2.close()

'''
运行结果:

[
    {
        "姓名": "李四",
        "语文": "90",
        "数学": "90",
        "英语": "90",
        "总分": "270",
        "排名": "1"
    },
    {
        "姓名": "张三",
        "语文": "80",
        "数学": "80",
        "英语": "80",
        "总分": "240",
        "排名": "2"
    },
    {
        "姓名": "赵六",
        "语文": "70",
        "数学": "80",
        "英语": "90",
        "总分": "240",
        "排名": "3"
    },
    {
        "姓名": "王五",
        "语文": "70",
        "数学": "70",
        "英语": "70",
        "总分": "210",
        "排名": "4"
    }
]
'''