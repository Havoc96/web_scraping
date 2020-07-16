# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath(
            '//div[@class="col-sm-6 col-md-4 m-p-product"]')
        for product in products:
            product_name = product.xpath('.//div[2]/p/a/text()').get()
            product_url = product.xpath('.//div[2]/p/a/@href').get()
            product_imageLink = product.xpath('.//div/a/img[1]/@src').get()
            product_price = product.xpath('.//div[2]/div/span/text()').get()

            yield{
                'product_name': product_name,
                'product_url': product_url,
                'product_imageLink': product_imageLink,
                'product_price': product_price
            }

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
