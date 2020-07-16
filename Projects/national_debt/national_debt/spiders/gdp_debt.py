# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["www.worldpopulationreview.com/"]
    start_urls = [
        "http://worldpopulationreview.com/countries/countries-by-national-debt/"
    ]

    def parse(self, response):
        rows = response.xpath("//tr")
        for row in rows:
            country_name = row.xpath(".//td/a/text()").get()
            national_debt = row.xpath(".//td[2]/text()").get()

            yield {"country_name": country_name,
                   "national_debt": national_debt
                   }
