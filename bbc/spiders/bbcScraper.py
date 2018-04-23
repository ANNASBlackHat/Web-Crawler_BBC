import scrapy

class NewsSpider(scrapy.Spider):
    name = "bbc"
    start_urls = [
        'http://www.bbc.com/',
    ]

    def parse(self, response):
        for content in response.css('div.media__content') :
            summary = content.css(".media__summary::text").extract_first()
            if summary is not None:
                summary = summary.strip()
            yield {
                'title': content.css('a.media__link::text').extract_first().strip(),
                'summary' : summary,
                'link': content.css("a::attr(href)").extract_first(),
            }
