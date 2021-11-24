import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Brief_Scraping_Allocine import methods

''' 
    This spider aims to extract a selected set of data from a list of the best movies on IMDb
'''
class BestTvShowsSpider(CrawlSpider):
    name = 'best_tv_shows'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//td[@class="titleColumn"]']), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1/text()').get()
        item['release_date'] = response.xpath('//li[@data-testid="title-details-releasedate"]/div/ul/li/a/text()').get()
        item['target_audience'] = response.xpath('//ul[@class="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt"]/li[3]/a/text()').get()
        item['length'] = "".join(response.xpath('//ul[@class="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt"]/li[4]/text()').getall())
        item['length'] = methods.minutify(item['length'])
        item['rating'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').get()
        item['synopsis'] = response.xpath('//span[@class="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA"]/text()').get()
        item['genres'] = response.xpath ('//a[@class="GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt"]/span/text()').getall()
        item['staring'] = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        item['original_language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').get()
        item['original_country'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').get()
        item['original_title'] = response.xpath('//div[@class="OriginalTitle__OriginalTitleText-jz9bzr-0 llYePj"]/text()').get()
        
        # Basic formating of the string scraped from the website
        if item['original_title']:
            item['original_title'] = re.findall(r'Original title: (.*)', item['original_title'])[0]
        seasons = response.xpath('//select[@id="browse-episodes-season"]/option[2]/text()').get()
        if seasons:
            item['nb_seasons'] = seasons
        else:
            item['nb_seasons'] = 1
        item['nb_episodes'] = response.xpath('//div[@data-testid="episodes-header"]/a/h3/span/text()').get()
                
        return item