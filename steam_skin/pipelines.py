# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class SteamSkinPipeline(object):
    """
        SteamSkinPipeline
        """
    def process_item(self, item, spider):
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
        item.do_insert(**spider.settings['DATABASE_SETTINGS']['mysql'])
        return item

