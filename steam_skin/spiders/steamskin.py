# -*- coding: utf-8 -*-
import scrapy
from steam_skin.items import SteamSkinItem


class SteamSkinSpider(scrapy.Spider):
    name = 'steamskin'
    start_urls = ["https://steamcommunity.com/market/"]

    def parse(self, response):
        """

        :param response:
        :return:
        """
        item = SteamSkinItem()
        yield item

