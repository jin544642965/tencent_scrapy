# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# 默认管道是没有启用的，需要去setting启用管道，才能找到创建的文件
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# 将系统默认格式设为utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class TencentPipeline(object):

    # 创建一个初始化方法，便于将item写入json文件，__init__系统默认隐藏的
    def __init__(self):
        # 初始化创建json文件
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        # 不用ascii编码打开，json.dumps将字典转化为字符串
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)          # 写的时候里面有中文需要存入格式为utf-8
        return item

    # 创建爬虫关闭时的一个方法。
    def close_spider(self, spider):
        self.f.close()