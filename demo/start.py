"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: start.py
@time: 2020/5/20 0020
"""
from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'qsbk', '--nolog'])
