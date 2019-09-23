# -*- coding: utf-8 -*-
import pymysql
from . import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):

        print(item['name'],item['star'],item['time'])

        return item

class MaoyanMysqlPipeline(object):
    def open_spider(self,spirde):
        self.db = pymysql.connect(
            host = settings.HOST,
            port = settings.PORT,
            user = settings.USER,
            password = settings.PWD,
            database = settings.DB,
            charset = settings.CHARSET,
        )
        self.cursor = self.db.cursor()


    def process_item(self, item, spider):
        sql = 'insert into filmtab values(%s,%s,%s)'
        L = [
            item['name'],
            item['star'],
            item['time'],
        ]
        self.cursor.execute(sql,L)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
