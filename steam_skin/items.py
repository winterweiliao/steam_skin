# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import pymysql
from settings import DATABASE_SETTINGS


class SteamSkinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
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

    def do_insert(self):
        """
        将数据插入到数据库
        :return:
        """
        # conn = pymysql.connect(self.db_kwargs)
        # cursor = conn.cursor()
        # sql = u"select * from goods_trade where market_name='%s' and trade_price='%s' and trade_time='%s'"
        # sql = sql % (self['market_name'], self['trade_price'], self['trade_time'], )
        # cursor.execute(sql)
        # if cursor.fetchone():
        #     cursor.close()
        #     conn.close()
        #     return
        fields = u""
        values = u""
        for key, value in self.items():
            fields += u"%s," % key
            values += u"'%s'," % value
        fields = fields.rstrip(u",")
        values = values.rstrip(u",")

        sql = u"insert into goods_trade(%s) values (%s)" % (fields, values)
        self.execute(sql)

    def do_update(self):
        """
        将数据更新到数据库
        :return:
        """
        pass

    def execute(self, sql):
        """

        :param sql:
        :return:
        """
        conn = pymysql.connect(**DATABASE_SETTINGS['mysql'])
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
