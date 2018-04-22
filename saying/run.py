from scrapy import cmdline

cmd_str = 'scrapy crawl quotes'
cmdline.execute(cmd_str.split(' '))