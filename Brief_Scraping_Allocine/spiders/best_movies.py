import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.allocine.fr/film/meilleurs/']
    start_urls = ['http://www.allocine.fr/film/meilleurs/']

    rules = (
        Rule(LinkExtractor(allow='film/'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {
            'title':response.xpath('//h2/a[@class="meta-title-link"]/text()').getall()
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
