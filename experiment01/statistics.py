"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: statistics.py
@time: 2020/3/25 0025
"""
import jieba

counts = {}
txt = open("static/活着.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
