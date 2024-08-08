from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.crawler import CrawlerProcess
import re

 class SpiderSpider(CrawlSpider):
     start_urls = ['https://create.roblox.com/docs']


class SpiderSpider(CrawlSpider):
    name= "sites"
    #allowed_domains = base_links

    le = LinkExtractor(allow_domains = base_links, unique=True)

    #rules = [Rule(le, callback='parse_all_subsites', follow=True)]
    rules = [Rule(le, callback='parse_all_subsites', follow=False)]

    def parse_all_subsites(self, response):
        #for link in response.css('a::attr(href)'):
        extracted_links = self.le.extract_links(response)
        pages = set()

        for link in extracted_links:
            pages.add(link.url)

        link_list.append(pages)


process = CrawlerProcess()

#iterates over every link and adds list of links of every sub-site to link_list
for link in links:

    process.crawl(SpiderSpider, start_urls=link)
    process.start()
