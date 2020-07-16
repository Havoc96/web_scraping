# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/electronics-c-597.html']

    def parse(self, response):
        products = response.xpath('//div[@class="p_box_wrapper"]/li')
        for product in products:
            title = product.xpath('.//a[2]/text()').get()
            url = product.xpath('.//a[2]/@href').get()
            original_price = product.xpath('.//div[2]/span[2]/text()').get()
            discounted_price = product.xpath('.//div[2]/span[1]/text()').get()

            yield{
                'title': title,
                'url': response.urljoin(url),
                'original_price': original_price,
                'discounted_price': discounted_price
            }

        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
