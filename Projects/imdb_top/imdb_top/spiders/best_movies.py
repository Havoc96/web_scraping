# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'Duration': response.xpath("normalize-space((//time)[1]/text())").get(),
            'Genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'Released': response.xpath("//div[@class='subtext']/a[last()]/text()").get(),
            'Link': response.url
        }   
    