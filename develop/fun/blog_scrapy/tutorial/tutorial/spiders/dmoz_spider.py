import scrapy

from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        for sel in response.xpath("//fieldset[@class='fieldcap']/ul/li"):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').re('-\s([^\n]*?)\\n')

            yield item
