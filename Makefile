all:
	rm output.json
	scrapy crawl -o output.json alcoholics-anonymous
