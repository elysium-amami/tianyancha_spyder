import os, json, sys
import scrapy
def get_gudong(select):
    trs=select.xpath('//*[@id="_container_holderCount"]/div/table/tbody/tr')
    Ltemp=[]
    for t in trs:
        temp = {}
        temp['股东']=t.xpath('./td[2]/table/tbody/tr/td[2]/a/text()').extract_first()
        temp['出资比例']=t.xpath('./td[3]//span/text()').extract_first()
        temp['认缴出资']=t.xpath('./td[4]//span/text()').extract_first()
        Ltemp.append(temp)
    return Ltemp