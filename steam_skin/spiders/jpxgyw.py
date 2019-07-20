# -*- coding: utf-8 -*-

import datetime
from urllib.parse import urljoin
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from ..items import ImageItem


class MeiNvSpider(RedisSpider):
    name = 'jpxgyw'
    allowed_domains = ["www.jpxgyw.com", "www.xgmn5.com", "img.xgmn5.com"]

    def parse(self, response):
        href_list = response.xpath('//a/@href').extract()
        for href in href_list:
            url = urljoin(response.url, href)
            yield Request(url, callback=self.parse_image)

    def parse_image(self, response):
        img_list = response.xpath('//img[starts-with(@src,"/uploadfile")]')
        for img in img_list:
            src = img.xpath('./@src').extract_first()
            name = img.xpath('./@alt').extract_first()

            url = urljoin(response.url, src)
            item = ImageItem()
            item['image_url'] = url
            item['image_urls'] = [url]
            item['name'] = name
            item['created_at'] = datetime.datetime.now()
            item['updated_at'] = datetime.datetime.now()
            yield item

        href_list = response.xpath('//a/@href').extract()
        for href in href_list:
            url = urljoin(response.url, href)
            yield Request(url)
            yield Request(url, callback=self.parse_image)
