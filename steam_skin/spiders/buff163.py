# -*- coding: utf-8 -*-
import scrapy
import pymysql
import json
import time
import datetime
from steam_skin.items import Buff163Item


class Buff163Spider(scrapy.Spider):
    name = 'buff163'
    allowed_domains = ["163.buff.com"]
    # start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def start_requests(self):
        """
        重新构造start_urls
        :return:
        """
        db_kwargs = self.settings['DATABASE_SETTINGS']['mysql']
        conn = pymysql.connect(**db_kwargs)
        # 创建一个游标对象
        cursor = conn.cursor()
        cursor.execute('select game, goods_id_at_buff, market_name, id, exterior from goods_info')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        for game, goods_id_at_buff, market_name, _id, exterior in data:
            url = 'https://buff.163.com/api/market/goods/bill_order?game=%s&goods_id=%d'
            url = url % (game, goods_id_at_buff)
            yield scrapy.Request(url, dont_filter=True, meta={
                'market_name': market_name,
                'id': _id,
                'exterior': exterior,
            })

    def parse(self, response):
        result = json.loads(response.body)
        data = result.get('data')
        for _item in data.get('items'):
            item = Buff163Item()
            item['market_name'] = response.meta['market_name']
            item['exterior'] = response.meta['exterior']
            item['app_code'] = _item['appid']
            item['game'] = _item['game']
            item['goods_info_id'] = response.meta['id']
            item['goods_id_at_buff'] = _item['goods_id']
            item['trade_id'] = _item['id']
            item['trade_price'] = _item['price']
            item['trade_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_item['transact_time']))
            item['seller_id'] = _item['seller_id']
            now = datetime.datetime.now()
            item['create_at'] = now
            item['update_at'] = now
            yield Buff163Item(item)

