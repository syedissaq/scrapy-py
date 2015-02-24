import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
import scrapy
from dcrawler.items import DcrawlerItem
class CricketSpider(scrapy.Spider):
    name = "cri"
    allowed_domains = ["espncricinfo.com"]
    start_urls = [
        "http://stats.espncricinfo.com/ci/content/records/335432.html"
    ]
    def parse(self, response):
        item = DcrawlerItem()
        # i=0
        for sel in response.xpath("""//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr"""):
            link= sel.xpath("td[1]/a/@href").extract()
            link.insert(0,"http://www.espncricinfo.com")
            item['team1']=''.join(link)
            print "done"
            r.lpush('listone',item['team1'])