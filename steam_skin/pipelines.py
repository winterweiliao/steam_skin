# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from steam_skin import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class SteamSkinPipeline(object):

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


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['image_url']:
            yield Request(image_url)

