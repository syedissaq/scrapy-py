# -*- coding: utf-8 -*
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
import scrapy
from scrapy_redis_cricket_data.items import CricketrecurItem
# result=r.lpop("url:l:1:day:cr")
# for i in range(0,3000):
#     result=r.lpop("url:l:1:day:cr")
l=[]
for i in range(0,len(r.lrange("url:l:1:day:cric",0,-1))):
    result =r.lpop("url:l:1:day:cric")
    l.append(result)
    r.lpush("url:l:1:day:cric",result)
class PakSpider(scrapy.Spider):
    name = "cri"
    start_urls = l
    def parse(self, response):
        i=0
        item = CricketrecurItem()
        item['matchid']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[2]/div[1]/a[1]/text()').extract()
        item['toss']= response.xpath('//*[@id="full-scorecard"]/div[3]/div/div/div[1]/span[1]/text()').extract()
        item['daynight']=  response.xpath('//*[@id="full-scorecard"]/div[1]/div[2]/div[3]/text()').extract()
        item['ground']=response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[1]/a/text()').extract()
             
        i=0
        total=0
        p=0
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]"""%x
            for sel in response.xpath(c): 
                i=i+2 
        i=i-2
        for x in range(2,i+1,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]"""%x
            for sel in response.xpath(c): 
                t=  sel.xpath('td[4]/text()').extract() 
                k=int(t[0])
                total=total+k
        i=i+2
        n=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%i).extract()
        ltotal=total+int(n[0])
        item['totalrunistinning']=ltotal
           
        i=0
        total=0
        p=0
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]"""%x
            for sel in response.xpath(c): 
                i=i+2 
        i=i-2
        for x in range(2,i+1,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]"""%x
            for sel in response.xpath(c): 
                t=  sel.xpath('td[4]/text()').extract() 
                k=int(t[0])
                total=total+k
        i=i+2
        n=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%i).extract()
        ltotal=total+int(n[0])
        item['totalrunsecondinning']=ltotal
        
        item['istbating']=     response.xpath('//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[1]/th[2]/text()').extract()
        item['secondbating']=  response.xpath('//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[1]/th[2]/text()').extract()  
        item['won']=  response.xpath('//*[@id="full-scorecard"]/div[1]/div[1]/div[3]/text()').extract()
        
        lr1=[]
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]"""%x
            for sel in response.xpath(c):
                x=sel.xpath('td[4]/text()').extract()
                lr1.append(int(x[0]))
        print type(lr1[0])
        print lr1
        x=lr1[0]
        xi=0
        for i in range(0,len(lr1)):
            if lr1[i] > x:
                x=lr1[i]
                xi=i
        yi=xi+xi+2        
        print xi        
        if xi==0:
          yi=2
          item['iisttoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['iisttoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['iisttoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['iisttoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()      
        
        lr1[xi]=0
        x=lr1[0]
        xi=0
        for i in range(0,len(lr1)):
            if lr1[i] > x:
                x=lr1[i]
                xi=i
        yi=xi+xi+2        
        if xi==0:
          yi=2
          item['isecondtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['isecondtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['isecondtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['isecondtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        lr1[xi]=0
        print lr1
        x=lr1[0]
        xi=0
        for i in range(0,len(lr1)):
            if lr1[i] > x:
                x=lr1[i]
                xi=i
        yi=xi+xi+2
        if xi==0:
          yi=2
          item['ithirdtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['ithirdtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['ithirdtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[4]/text()"""%yi).extract()
          item['ithirdtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[1]/tr[%d]/td[2]/a/text()"""%yi).extract()      
        
        lr3=[]
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]"""%x
            for sel in response.xpath(c):
                x=sel.xpath('td[6]/text()').extract()
                lr3.append(int(x[0]))
        print type(lr3[0])
        print lr3
        x=lr3[0]
        xi=0
        for i in range(0,len(lr3)):
            if lr3[i] > x:
                x=lr3[i]
                xi=i
        yi=xi+xi+2        
        print xi        
        if xi==0:
          yi=2
          item['iisttopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['iisttopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['iisttopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['iisttopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        lr3[xi]=0
        x=lr3[0]
        xi=0
        for i in range(0,len(lr3)):
            if lr3[i] > x:
                x=lr3[i]
                xi=i
        yi=xi+xi+2       
        if xi==0:
          yi=2
          item['isecondtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['isecondtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['isecondtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['isecondtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        lr3[xi]=0
        x=lr3[0]
        xi=0
        for i in range(0,len(lr3)):
            if lr3[i] > x:
                x=lr3[i]
                xi=i
        yi=xi+xi+2
        if xi==0:
          yi=2
          item['ithirdtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['ithirdtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:
          item['ithirdtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[6]/text()"""%yi).extract()
          item['ithirdtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[2]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        lr2=[]
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]"""%x
            for sel in response.xpath(c):
                x=sel.xpath('td[4]/text()').extract()
                lr2.append(int(x[0]))
        x=lr1[0]
        xi=0
        for i in range(0,len(lr2)):
            if lr2[i] > x:
                x=lr2[i]
                xi=i
        yi=xi+xi+2        
        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['sisttoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['sisttoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['sisttoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['sisttoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['sisttoprunerbatsman']
        print item['sisttoprunerbatsmanname']
        
        print xi
        lr2[xi]=0
        print lr2
        x=lr2[0]
        xi=0
        for i in range(0,len(lr2)):
            if lr2[i] > x:
                x=lr2[i]
                xi=i
        yi=xi+xi+2 

        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['ssecondtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['ssecondtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['ssecondtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['ssecondtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['ssecondtoprunerbatsman']
        print item['ssecondtoprunerbatsmanname']

        #11##################################
        print xi
        lr2[xi]=0
        print lr2
        x=lr2[0]
        xi=0
        for i in range(0,len(lr2)):
            if lr2[i] > x:
                x=lr2[i]
                xi=i
        yi=xi+xi+2 

        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['sthirdtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['sthirdtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['sthirdtoprunerbatsman']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[4]/text()"""%yi).extract()
          item['sthirdtoprunerbatsmanname']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[3]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['sthirdtoprunerbatsman']
        print item['sthirdtoprunerbatsmanname']
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #IIIIIIIIIIIIIIIIIIIIIIIRRRRRRRRRRRRRRRRRRRIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        lr4=[]
        for x in range(2,25,2):
            c = """//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]"""%x
            for sel in response.xpath(c):
                x=sel.xpath('td[6]/text()').extract()
                lr4.append(int(x[0]))
        print type(lr4[0])
        print lr4
        x=lr4[0]
        xi=0
        for i in range(0,len(lr4)):
            if lr4[i] > x:
                x=lr4[i]
                xi=i
        yi=xi+xi+2        
        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['sisttopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['sisttopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['sisttopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['sisttopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['sisttopbowler']
        print item['sisttopbowlername']

        print xi
        lr4[xi]=0
        print lr4
        x=lr4[0]
        xi=0
        for i in range(0,len(lr4)):
            if lr4[i] > x:
                x=lr4[i]
                xi=i
        yi=xi+xi+2 

        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['ssecondtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['ssecondtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['ssecondtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['ssecondtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['ssecondtopbowler']
        print item['ssecondtopbowlername']

        #11##################################
        print xi
        lr4[xi]=0
        print lr4
        x=lr4[0]
        xi=0
        for i in range(0,len(lr4)):
            if lr4[i] > x:
                x=lr4[i]
                xi=i
        yi=xi+xi+2 

        print xi        
        if xi==0:
          yi=2
                                                    # //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[4]/text()
          item['sthirdtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['sthirdtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()
        else:  #                                                    //*[@id="full-scorecard"]/div[2]/div/table[1]/tbody/tr[10]/td[2]/a/text()
          item['sthirdtopbowler']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[6]/text()"""%yi).extract()
          item['sthirdtopbowlername']=response.xpath("""//*[@id="full-scorecard"]/div[2]/div/table[4]/tr[%d]/td[2]/a/text()"""%yi).extract()      
                 
        print  item['sthirdtopbowler']
        print item['sthirdtopbowlername']
        r.lpush("data:one:day:match",item)
        