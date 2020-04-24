"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo01.py
@time: 2020/4/24 0024
"""
'''
绘制词云图片
'''

import wordcloud
import jieba
from imageio import imread

mask = imread("./qqqe.png")
c = wordcloud.WordCloud(
    font_path="msyh.ttc",
    width=1000,
    height=700,
    mask=mask,
    max_words=30,
    background_color="white"
)

c.generate(" ".join(
    filter(lambda x: x not in [i.strip() for i in
                               open("./stopwords.txt", "r", encoding="utf-8").readlines()],
           jieba.lcut(
               open("./chat.txt", "r", encoding="utf-8").read()))))

c.to_file("pw.jpg")
