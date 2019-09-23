from scrapy import cmdline
# 保存为csv文件
# cmdline.execute('scrapy crawl maoyan2 -o maoyan.csv'.split())

# 保存为JSON 文件
cmdline.execute('scrapy crawl maoyan2 -o maoyan.json'.split())
# cmdline.execute('scrapy crawl maoyan2'.split())