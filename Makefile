all:
	rm output.json
	scrapy crawl -o output.json alcoholics-anonymous
	sed -i '1s;^;{"data":;' output.json
	echo "}" >> output.json
