"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo02.py
@time: 2020/5/6 0006
"""
import requests as rq
from bs4 import BeautifulSoup as Bs
import pandas as pd
import numpy as np


# 获取数据,就是通过访问网页,把他的html源代码拿过来
def getData(resLoc):
    rp = rq.get(resLoc)
    rp.encoding = 'utf-8'
    return rp.text


# 最关键的部分: 数据处理,我们的目标是将文本格式的 html 网页转化为表格的形式;
def dataProcessing(html, num):
    bs = Bs(html, features='lxml')
    # 包含表头的列表
    table = bs.table.find_all('tr', limit=num, recursive=True)
    table_head = table[0]
    # print(table_head)
    # 看一下表头是什么:
    # <tr>
    #   <th style="text-align: center;">排名</th>
    #   <th style="text-align: center;">学校名称</th>
    #   <th class="hidden-xs" style="text-align: center; width: 80px;">省市</th>
    #   <th style="text-align: center;">总分</th>
    #   <th class="hidden-xs" style="text-align: center; width: 265px;">指标得分<br/>
    #   <select class="form-control" id="select-indicator-type" name="type" style="text-align: left;">
    #     <option selected="selected" title="生源质量（新生高考成绩得分）" value="indicator5">生源质量（新生高考成绩得分）</option>
    #     <option title="培养结果（毕业生就业率）" value="indicator6">培养结果（毕业生就业率）</option>
    #     <option title="社会声誉（社会捐赠收入·千元）" value="indicator7">社会声誉（社会捐赠收入·千元）</option>
    #     <option title="科研规模（论文数量·篇）" value="indicator8">科研规模（论文数量·篇）</option>
    #     <option title="科研质量（论文质量·FWCI）" value="indicator9">科研质量（论文质量·FWCI）</option>
    #     <option title="顶尖成果（高被引论文·篇）" value="indicator10">顶尖成果（高被引论文·篇）</option>
    #     <option title="顶尖人才（高被引学者·人）" value="indicator11">顶尖人才（高被引学者·人）</option>
    #     <option title="科技服务（企业科研经费·千元）" value="indicator12">科技服务（企业科研经费·千元）</option>
    #     <option title="成果转化（技术转让收入·千元）" value="indicator13">成果转化（技术转让收入·千元）</option>
    #     <option title="学生国际化（留学生比例） " value="indicator14">学生国际化（留学生比例）</option>
    #   </select>
    #   </th>
    # </tr>
    # 去掉表头,只要表体
    table_body = table[1:]
    # print(table_body)
    # 看一下每一条 tr 里面是什么?
    # [ <tr class="alt">
    #   <td>1</td> --排名
    #   <td><div align="left">清华大学</div></td> --学校名称
    #   <td>北京</td> --省市
    #   <td>94.6</td> --总分
    #   <td class="hidden-xs need-hidden indicator5">100.0</td> --生源质量
    #   <td class="hidden-xs need-hidden indicator6" style="display: none;">98.30%</td> --培养结果
    #   <td class="hidden-xs need-hidden indicator7" style="display: none;">1589319</td> --社会声誉
    #   <td class="hidden-xs need-hidden indicator8" style="display: none;">48698</td> --科研规模
    #   <td class="hidden-xs need-hidden indicator9" style="display: none;">1.512</td> --科研质量
    #   <td class="hidden-xs need-hidden indicator10" style="display: none;">1810</td> --顶尖成果
    #   <td class="hidden-xs need-hidden indicator11" style="display: none;">126</td> --顶尖人才
    #   <td class="hidden-xs need-hidden indicator12" style="display: none;">1697330</td> --科技服务
    #   <td class="hidden-xs need-hidden indicator13" style="display: none;">302898</td> --成果转化
    #   <td class="hidden-xs need-hidden indicator14" style="display: none;">6.81%</td> --学生国际化
    # </tr> ]
    # for tr in table_body:
    # 我们可以无视上面标签中的属性值,只关注内容
    # 也就是说对于table_body中的每一个tr标签,我们要做的是取出来其中的td中的content,作为二维列表
    universityList = []
    for tr in table_body:
        tds = tr.find_all('td')
        # tds 的结果是:
        # print(tds)
        # [ <td>1</td>,
        #   <td><div align="left">清华大学</div></td>,
        #   <td>北京</td>, <td>94.6</td>,
        #   <td class="hidden-xs need-hidden indicator5">100.0</td>,
        #   <td class="hidden-xs need-hidden indicator6" style="display: none;">98.30%</td>,
        #   <td class="hidden-xs need-hidden indicator7" style="display: none;">1589319</td>,
        #   <td class="hidden-xs need-hidden indicator8" style="display: none;">48698</td>,
        #   <td class="hidden-xs need-hidden indicator9" style="display: none;">1.512</td>,
        #   <td class="hidden-xs need-hidden indicator10" style="display: none;">1810</td>,
        #   <td class="hidden-xs need-hidden indicator11" style="display: none;">126</td>,
        #   <td class="hidden-xs need-hidden indicator12" style="display: none;">1697330</td>,
        #   <td class="hidden-xs need-hidden indicator13" style="display: none;">302898</td>,
        #   <td class="hidden-xs need-hidden indicator14" style="display: none;">6.81%</td> ]
        # 可以看到是一个列表,我们获取每一个 td 标签的 content
        contents = [td.contents for td in tds]
        # for td in tds:
        #     print(td.contents)
        # 得到的结果如下:
        # ['1']
        # [<div align="left">清华大学</div>]
        # ['北京']
        # ['94.6']
        # ['100.0']
        # ['98.30%']
        # ['1589319']
        # ['48698']
        # ['1.512']
        # ['1810']
        # ['126']
        # ['1697330']
        # ['302898']
        # ['6.81%']
        # 但是有一个问题就是 [<div align="left">清华大学</div>] 这里有一个 div 标签,我们要把它替换成他里面的元素值
        contents[1] = contents[1][0].contents
        # 大家注意我们现在还在for循环当中哦,我们要这些遍历到的contents存到外面的变量中才能保存起来
        universityList.append(contents)

    # 现在我们得到的列表就是类似于这种形式[[[清华], [1], ...], [[北大], [2], ...], ...]
    # print(universityList)
    # 但是现在还没有把表头加上,现在我们加上表头,但是表头还是那个乱七八糟的形式,所以我们要先处理一下

    # 这里为什么只要四个呢? 因为第五个是下拉选框,我们后面再单独处理
    ths = table_head.find_all('th', limit=4)
    # 这里是表头的前四个元素 [['排名'], ['学校名称'], ['省市'], ['总分']], th_four 代表前四个th
    thf = [th.contents for th in ths]
    # 下面处理下拉框中的元素 option
    options = [op.contents for op in table_head.find_all('option', recursive=True)]
    # print(options)
    # [ ['生源质量（新生高考成绩得分）'],
    #   ['培养结果（毕业生就业率）'],
    #   ['社会声誉（社会捐赠收入·千元）'],
    #   ['科研规模（论文数量·篇）'],
    #   ['科研质量（论文质量·FWCI）'],
    #   ['顶尖成果（高被引论文·篇）'],
    #   ['顶尖人才（高被引学者·人）'],
    #   ['科技服务（企业科研经费·千元）'],
    #   ['成果转化（技术转让收入·千元）'],
    #   ['学生国际化（留学生比例）'] ]

    # 好了,现在我们合并表头
    for i in options:
        thf.append(i)
    # print(thf)
    # 下面的问题是, 我们有了表头列表 thf(二维),有了表体列表 universityList(三维), 怎么把它们合并呢?
    # thf: [['排名'], ['学校名称'], ['省市'], ['总分'], ['生源质量（新生高考成绩得分）'], ['培养结果（毕业生就业率）'], ['社会声誉（社会捐赠收入·千元）'], ['科研规模（论文数量·篇）'], ['科研质量（论文质量·FWCI）'], ['顶尖成果（高被引论文·篇）'], ['顶尖人才（高被引学者·人）'], ['科技服务（企业科研经费·千元）'], ['成果转化（技术转让收入·千元）'], ['学生国际化（留学生比例）']]
    # universityList: [
    #                   [['1'], ['清华大学'], ['北京'], ['94.6'], ['100.0'], ['98.30%'], ['1589319'], ['48698'], ['1.512'], ['1810'], ['126'], ['1697330'], ['302898'], ['6.81%']],
    #                   [['2'], ['北京大学'], ['北京'], ['76.5'], ['95.2'], ['98.07%'], ['570497'], ['47161'], ['1.409'], ['1402'], ['100'], ['554680'], ['14445'], ['6.15%']]
    #                 ]
    # 但是还有一个问题就是DataFrame是二维结构,我们这里是三维结构,显然需要降维打击!
    # 我们把最里面的列表可以转化为字符串,实现降维
    thf = ["".join(th) for th in thf]
    # universityList = ["".join(attr) for attr in [university for university in universityList]]
    # print(universityList)|
    univList = []
    for university in universityList:
        university = ["".join(attr) for attr in university]
        univList.append(university)

    pd_universityList = pd.DataFrame(np.array(univList), columns=thf)

    return pd_universityList
    # 显示所有列
    # pd.set_option('display.max_columns', None)
    # 显示所有行
    # pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    # pd.set_option('max_colwidth', 100)
    # print(pd_universityList)


# 负责保存数据到本地磁盘
def saveData(data):
    data.to_csv('university.csv', index=False)
    data.to_excel('university.xlsx', index=False)


def main(num):
    # 由于该网站最多有550个大学,所以输入的数字不能大于550,否则什么也不做
    if num >= 550:
        print("数量不能大于550")
        return
    else:
        url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'
        # 获取数据
        text = getData(url)
        # 处理数据, num 是你要爬取前多少名大学的排名信息
        universityList = dataProcessing(text, num + 1)
        # 保存数据
        saveData(universityList)
        print("文件保存成功!")


# 测试,爬取前10名大学的信息
main(10)
