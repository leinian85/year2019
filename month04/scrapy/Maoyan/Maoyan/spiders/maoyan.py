# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']
    count = 0

    def parse(self, response):
        item = MaoyanItem()
        datas = response.xpath('//dl[@class="board-wrapper"]/dd')
        self.offset = 0
        for data in datas:
            # item['name'] = data.xpath('./a/@title').extract()[0].strip()
            # item['star'] = data.xpath('.//p[@class="star"]/text()').extract_first().strip()
            # item['time'] = data.xpath('.//p[@class="releasetime"]/text()').get().strip()
            item['name'] = data.xpath('./a/@title').get().strip()
            item['star'] = data.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = data.xpath('.//p[@class="releasetime"]/text()').get().strip()
            self.count += 1
            yield item

        while self.offset <=80 :
            self.offset += 10
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            yield scrapy.Request(
                url = url,
                callback=self.parse
            )

        print(self.count)

