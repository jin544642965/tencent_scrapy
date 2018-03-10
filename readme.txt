项目要求：
爬取腾讯网站的招聘职位，职位链接，招聘类别，招聘人数，招聘地点，发布时间。

编写爬虫的流程
1.创建项目
scrapy startproject tencent_scrapy
2.创建爬虫
scrapy genspider tencent
3.编写items（在项目根目录）
定义保存数据的字段
name = scrapy.Field()
4.编写爬虫spiders/tencent.py
  yield item --->管道处理; yield Request --->调度器处理
5.编写settings.py，启用ITEM_PIPELINES，设置相关配置信息(如USER_AGENT等)
设置user-agent，伪装成浏览器，抵御基本的反爬
ROBOTSTXT_OBEY = False # 关闭反爬robbit协议
CONCURRENT_REQUESTS = 400  并发连接请求改为400，同时对400个连接进行请求
5.运行爬虫命令：scrapy crawl tencent

