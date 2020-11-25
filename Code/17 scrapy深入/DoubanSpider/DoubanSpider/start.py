from scrapy import cmdline

cmdline.execute('scrapy crawl douban'.split())
# cmdline.execute('scrapy crawl tuijian -o data.csv'.split()) # -o 做测试的时候用
