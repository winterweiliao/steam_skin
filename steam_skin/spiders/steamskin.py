# -*- coding: utf-8 -*-
import scrapy
from steam_skin.items import SteamSkinItem


class SteamSkinSpider(scrapy.Spider):
    name = 'steamskin'
    start_urls = ["https://steamcommunity.com/market/"]

    def parse(self, response):
        item = SteamSkinItem()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        yield item

