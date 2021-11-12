# -*- coding: utf-8 -*-
import scrapy


class BestsellerGlassesSpider(scrapy.Spider):
    name = 'bestseller_glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='p-title-block']/div[@class='mt-3']/div"):
            yield {
                'title': product.xpath(".//div[1]/div/a[1]/@title").get(),
                'price': product.xpath(".//div[2]/div/div[1]/span/text()").get(),
                'url': product.xpath(".//div[1]/div/a[1]/@href").get(),
            }

        next_page = response.xpath("//ul[@class='pagination']/li/a[@rel='next']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
