# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamSkinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class Buff163Item(scrapy.Item):
    # define the fields for your item here like:
    market_name = scrapy.Field()
    exterior = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    app_code = scrapy.Field()
    game = scrapy.Field()
    goods_info_id = scrapy.Field()
    goods_id_at_buff = scrapy.Field()
    trade_id = scrapy.Field()
    trade_price = scrapy.Field()
    trade_time = scrapy.Field()
    seller_id = scrapy.Field()
    site = scrapy.Field()
    create_at = scrapy.Field()
    update_at = scrapy.Field()

    class Meta:
        table_name = 'goods_trade'
