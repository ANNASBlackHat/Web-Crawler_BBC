# Web-Crawler_BBC
Crawling BBC webpage using Scrapy

#### Install Scrapy
```sh
pip install scrapy
```

#### Run Scrapy
```sh
scrapy runspider bbc/spiders/bbcScraper.py -o data.json
```

and then you should look an output inside data.json file. The file content data like this :
```sh
[{
		"title": "Armenian PM resigns after protests",
		"summary": "Serzh Sargsyan, who recently moved from president to PM, steps down after street protests against him.",
		"link": "/news/world-europe-43868433"
	},
  .......
```
