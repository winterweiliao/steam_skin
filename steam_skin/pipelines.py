# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import pymysql


class SteamSkinPipeline(object):
    """
    SteamSkinPipeline
    """
    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :return:
        """
        return item


class Buff163Pipeline(object):
    """
    Buff163Pipeline
    """
    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :return:
        """
        self.do_insert(item, spider)
        return item

    def do_insert(self, item, spider):
        """
        将数据插入到数据库
        :return:
        """
        fields = u""
        values = u""
        for key, value in item.items():
            fields += u"%s," % key
            values += u"'%s'," % value
        fields = fields.rstrip(u",")
        values = values.rstrip(u",")

        sql = u"insert into goods_trade(%s) values (%s)" % (fields, values)
        self.execute(sql, spider)

    def execute(self, sql, spider):
        """

        :param sql:
        :return:
        """
        conn = pymysql.connect(**spider.settings['DATABASE_SETTINGS']['mysql'])
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
