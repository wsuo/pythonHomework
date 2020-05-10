"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo03.py
@time: 2020/5/10 0010
"""
import requests as rq
from bs4 import BeautifulSoup as Bs
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


# 获取数据,就是通过访问网页,把他的html源代码拿过来
def getData(resLoc):
    rp = rq.get(resLoc)
    rp.encoding = 'utf-8'
    return rp.text


# 最关键的部分: 数据处理,我们的目标是将文本格式的 html 网页转化为表格的形式;
def dataProcessing(html, num):
    bs = Bs(html, features='lxml')

    # 获取 html 中 DOM 树的表格结构
    table = bs.table.tbody.find_all('tr', limit=num, recursive=True)
    universityList = []

    # 遍历该表格,筛选出我们需要的信息存储到 universityList 中
    for tr in table:
        tds = tr.find_all('td')
        contents = [td.contents for td in tds]
        contents[1] = contents[1][0].contents

        # 这里网页中是图片,但是可以通过截取字符串获取到国家的英文简写
        contents[2] = contents[2][0]['href'].split('/')[1].split('.')[0]
        contents = [''.join(i) for i in contents]
        # ['1', '哈佛大学', 'USA', '1', '100.0', '100.0', '100.0', '100.0', '100.0', '100.0', '78.2']
        universityList.append(contents)

    # 自己写表头,因为网站上爬太复杂了
    thf = ['世界排名', '学校', '国家', '在该国家的排名', '总分', '校友获奖', '教师获奖',
           '高被引学者', 'N&S论文', '国际论文', '师均表现']

    # 转化为 DataFrame 结构,因为这种结构很好转化为 Excel
    pd_universityList = pd.DataFrame(np.array(universityList), columns=thf)
    return pd_universityList


# 负责保存数据到本地磁盘
def saveData(data):
    data.to_excel('university.xlsx', index=False)


# 数据可视化
def can_view(universityList):
    # 将 pandas 数据类型转化为 numpy 数组
    data = np.array(universityList)

    # 获取 总分 数据项, 下面的也以此类推
    da1 = [eval(i[4]) for i in data]
    da2 = [eval(i[5]) for i in data]
    da3 = [eval(i[6]) for i in data]
    da4 = [eval(i[7]) for i in data]
    da5 = [eval(i[8]) for i in data]
    da6 = [eval(i[9]) for i in data]
    da7 = [eval(i[10]) for i in data]

    # 获取大学名称作为横坐标
    un = [i[1] for i in data]

    # 在 InitOpts 中可以设置主题样式和图表的宽度
    bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='2000px'))
           .add_xaxis(un)
           .add_yaxis('总分', da1)
           .add_yaxis('校友获奖', da2)
           .add_yaxis('教师获奖', da3)
           .add_yaxis('高被引学者', da4)
           .add_yaxis('N&S论文', da5)
           .add_yaxis('国际论文', da6)
           .add_yaxis('师均表现', da7)

           # 设置标题, AxisOpts 是设置横坐标的每一个数据项的倾斜程度
           .set_global_opts(title_opts=opts.TitleOpts(title="世界大学学术排名"),
                            xaxis_opts=opts.AxisOpts(name_rotate=60, name="大学名称", axislabel_opts={"rotate": 45}))
           )
    bar.render()


def main(num):
    # 由于该网站最多有 1000 个大学,所以输入的数字不能大于 1000 ,否则什么也不做
    if num >= 1000:
        print("数量不能大于1000")
        return
    else:
        url = 'http://www.zuihaodaxue.cn/ARWU2019.html'
        universityList = dataProcessing(getData(url), num)
        saveData(universityList)
        print("文件保存成功!")
        can_view(universityList)


# 测试,爬取前10名大学的信息
main(10)
