"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo01.py
@time: 2020/5/11 0011
"""
import requests as rq
from lxml import etree
import pandas as pd
import numpy as np


# 获取数据,就是通过访问网页,把他的html源代码拿过来
def getData(resLoc):
    rp = rq.get(resLoc)
    rp.encoding = 'utf-8'
    return rp.text


# 最关键的部分: 数据处理,我们的目标是将文本格式的 html 网页转化为表格的形式;
def dataProcessing(html, num):
    html = etree.HTML(html)

    # 获取表头 //thead//th[position() < 5] //thead//option
    th = html.xpath('//thead//th[position() < 5]/text()')
    th_select = html.xpath('//thead//option/text()')
    th.extend(th_select)

    # 大学名称
    univ = html.xpath('//tbody/tr/td/div/text()')[:num]

    # //tbody/tr[1]/td/text() 获取每一条记录的数值
    nums = [[j for j in html.xpath('//tbody/tr[' + str(i + 1) + ']/td/text()')] for i in range(num)]
    idx = 0
    for num in nums:
        num.insert(1, univ[idx])
        idx += 1

    # 转化为 DataFrame 结构,因为这种结构很好转化为 Excel
    pd_universityList = pd.DataFrame(np.array(nums), columns=th)
    return pd_universityList


# 负责保存数据到本地磁盘
def saveData(data):
    data.to_csv('university_china.csv', index=False)


def main(num):
    # 由于该网站最多有 1000 个大学,所以输入的数字不能大于 1000 ,否则什么也不做
    if num >= 1000:
        print("数量不能大于1000")
        return
    else:
        url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'
        universityList = dataProcessing(getData(url), num)
        saveData(universityList)
        print("文件保存成功!")


# 测试,爬取前10名大学的信息
main(10)
