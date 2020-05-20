# -*- coding: utf-8 -*-
import scrapy
# noinspection PyUnresolvedReferences
from demo.items import DemoItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'  # 运行的时候输入这个名字
    allowed_domains = ['qiushibaike.com']  # 允许的域名
    start_urls = ['https://www.qiushibaike.com/text/page/1/']  # 开始的 url
    base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in divs:
            author = div.xpath('.//h2/text()').get().strip()
            content = ''.join(div.xpath('.//div[@class="content"]/span[1]/text()').getall()).strip()
            # yield 的作用是将函数作为一个生成器,以后遍历的时候就会把数据一个一个的拿过去
            yield DemoItem(author=author, content=content)
        next_url = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)
