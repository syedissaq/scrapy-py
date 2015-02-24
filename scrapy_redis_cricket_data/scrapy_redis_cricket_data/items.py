# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CricketrecurItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    matchid=scrapy.Field()
    toss=scrapy.Field()
    daynight=scrapy.Field()
    ground=scrapy.Field()
    totalrunistinning=scrapy.Field()
    totalrunsecondinning=scrapy.Field()
    won=scrapy.Field()
    istbating=scrapy.Field()
    playedat=scrapy.Field()
    secondbating=scrapy.Field()
    iisttoprunerbatsman=scrapy.Field()
    iisttoprunerbatsmanname=scrapy.Field()
    isecondtoprunerbatsman=scrapy.Field()
    isecondtoprunerbatsmanname=scrapy.Field()
    ithirdtoprunerbatsman=scrapy.Field()
    ithirdtoprunerbatsmanname=scrapy.Field()
    iisttopbowler=scrapy.Field()
    iisttopbowlername=scrapy.Field()
    isecondtopbowler=scrapy.Field()
    isecondtopbowlername=scrapy.Field()
    ithirdtopbowler=scrapy.Field()
    ithirdtopbowlername=scrapy.Field()
    sisttoprunerbatsman=scrapy.Field()
    sisttoprunerbatsmanname=scrapy.Field()
    ssecondtoprunerbatsman=scrapy.Field()
    ssecondtoprunerbatsmanname=scrapy.Field()
    sthirdtoprunerbatsman=scrapy.Field()
    sthirdtoprunerbatsmanname=scrapy.Field()
    sisttopbowler=scrapy.Field()
    sisttopbowlername=scrapy.Field()
    ssecondtopbowler=scrapy.Field()
    ssecondtopbowlername=scrapy.Field()
    sthirdtopbowler=scrapy.Field()
    sthirdtopbowlername=scrapy.Field()