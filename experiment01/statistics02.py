"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: statistics02.py
@time: 2020/3/25 0025
"""
import jieba

counts = {}
txt = open("static/活着.txt", "r", encoding='utf-8').read()
# strip函数的作用是 删除前后的空格
stops = [i.strip() for i in open('static/stopwords/stopwords.txt', 'r', encoding='utf-8').readlines()]
words = jieba.lcut(txt)
for word in words:
    # 如果词组在停用字典中就跳过
    if word not in stops:
        # 跳过单个字符
        if len(word) == 1:
            continue
        # 同义词替换
        elif word == '老全' or word == '丈人':
            reword = '老全'
        else:
            reword = word
        counts[reword] = counts.get(reword, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
