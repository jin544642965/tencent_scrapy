# coding:utf-8
import scrapy
from Tencent.items import TencentItem


# 创建继承自scrapy.Spider类的爬虫
class TencentSpider(scrapy.Spider):
    # 爬虫名
    name = 'tencent'
    # 域名范围
    allowed_domains = ["tencent.com"]
    # 要爬取的固定的url
    baseURL = "https://hr.tencent.com/position.php?&start="
    # # 偏移量
    # offset = 0
    # # # 启始的url地址列表,单个地址爬取
    # # start_urls = [baseURL + str(offset)]

    # 批量爬取360页
    start_urls = [baseURL + str((i*10)) for i in range(0, 361)]

    # 前面请求发出去，定义处理响应
    def parse(self, response):
        # 定义提取的内容,用xpath提取html网页内容(职位名，链接，职位类别,工作地点，发布时间)
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # 迭代列表,对列表中每一个内容进行提取
        for node in node_list:
            # 提取td标签的内容，有4个td, 提取第一个td下的a标签中的文本内容,内容是列表，取第0个
            # extract是提取的意思

            # 实例化一个项目对象
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = "https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = node.xpath("./td[2]/text()").extract()[0]
            item['people_number'] = node.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = node.xpath("./td[4]/text()").extract()[0]
            item['publish_times'] = node.xpath("./td[5]/text()").extract()[0]
            # 每次循环返回一个item，交给管道文件处理（不用列表)。使用生成器,每循环一次转到另一个程序去处理，返回值item
            yield item
