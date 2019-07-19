# -*- coding: utf-8 -*-
import scrapy
from ..items import SteamSkinItem


class SteamSpider(scrapy.Spider):
    name = 'steam'
    start_urls = ["https://steamcommunity.com/market/"]

    def parse(self, response):
        """

        :param response:
        :return:
        """
        item = SteamSkinItem()
        yield item
