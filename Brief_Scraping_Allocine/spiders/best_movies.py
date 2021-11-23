import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.allocine.fr']
    start_urls = ['http://www.allocine.fr/film/meilleurs/']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths='//section[@class="section section-wrap gd-3-cols gd-gap-20"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=['//h2[@class="meta-title"]']), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination-item-holder"]')),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="titlebar-title titlebar-title-lg"]/text()').get()
        # item['release_date'] = response.xpath('//a[@class="xXx date blue-link"]').get()
        # item['target_audience'] = response.xpath('').get()
        # item['length'] = response.xpath('').get()
        # item['rating'] = response.xpath('').get()
        # item['synopsis'] = response.xpath('').get()
        # item['genre'] = response.xpath('').get()
        # item['staring'] = response.xpath('').getall()
        # item[''] = response.xpath('').get()
        # item[''] = response.xpath('').get()
        # item[''] = response.xpath('').get()
        # item[''] = response.xpath('').get()
        # item[''] = response.xpath('').get()
        # item[''] = response.xpath('').get()
        return item
