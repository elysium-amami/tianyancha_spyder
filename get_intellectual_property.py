import os, json, sys
import scrapy
def get_intellectual_property(select):
    temp = {}
    temp['商标信息'] = select.xpath('//*[@id="nav-main-tmCount"]/span[2]/text()').extract_first()
    temp['专利信息'] = select.xpath('//*[@id="nav-main-patentCount"]/span[2]/text()').extract_first()
    temp['软件著作权'] = select.xpath('//*[@id="nav-main-cpoyRCount"]/span[2]/text()').extract_first()
    temp['作品著作权'] = select.xpath('//*[@id="nav-main-copyrightWorks"]/span[2]/text()').extract_first()
    temp['网站备案'] = select.xpath('//*[@id="nav-main-icpCount"]/span[2]/text()').extract_first()
    return temp