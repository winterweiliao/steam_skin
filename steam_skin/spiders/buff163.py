# -*- coding: utf-8 -*-
import scrapy
from steam_skin.items import Buff163Item


class Buff163Spider(scrapy.Spider):
    name = 'buff163'
    allowed_domains = []
    start_urls = ['https://news.jxcn.cn/p/20190119/5712521.html?m=995a2b5083e2f563ed8db7b0c9294ebd']

    def parse(self, response):
        item = Buff163Item()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        yield item

