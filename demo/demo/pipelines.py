# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import json

# class DemoPipeline(object):
#     def process_item(self, item, spider):
#         json.dump(dict(item), self.file, ensure_ascii=False, indent=4)
#         self.file.write('\n')
#         return item
#
#     def open_spider(self, spider):
#         self.file = open('dz.json', 'w', encoding='utf-8')
#         print('爬虫开始')
#
#     def close_spider(self, spider):
#         self.file.close()
#         print('爬虫结束')

from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter


# class DemoPipeline(object):
#     def __init__(self):
#         self.file = open('dz.json', 'wb')
#         self.exporter = JsonItemExporter(self.file, ensure_ascii=False, encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫开始了')
#         # 使用二进制打开
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#         print('爬虫结束了')

class DemoPipeline(object):
    def __init__(self):
        self.file = open('dz.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('爬虫结束了')
