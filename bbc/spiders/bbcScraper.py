import scrapy

class NewsSpider(scrapy.Spider):
    name = "bbc"
    start_urls = [
        'http://www.bbc.com/',
    ]

    def parse(self, response):
        for content in response.css('div.media__content') :
            yield {
                'title': content.css('a.media__link::text').extract_first().strip(),
                'summary' : content.css(".media__summary::text").extract_first().strip(),
                'link' : content.css("a::attr(href)").extract_first(),
            }
