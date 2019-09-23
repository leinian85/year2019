# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']
    count = 0

    def start_requests(self):
        for i in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset={}'.format(i)
            yield scrapy.Request(
                url = url,
                callback=self.parse_html
            )

    def parse_html(self, response):
        item = MaoyanItem()
        datas = response.xpath('//dl[@class="board-wrapper"]/dd')
        self.offset = 0
        for data in datas:
            item['name'] = data.xpath('./a/@title').get().strip()
            item['star'] = data.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = data.xpath('.//p[@class="releasetime"]/text()').get().strip()
            self.count += 1
            yield item

