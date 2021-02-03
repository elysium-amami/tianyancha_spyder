import os, json, sys
import scrapy
def get_gongshang(select):
    trs = select.xpath('//*[@id="_container_baseInfo"]/table//tr')
    temp={}

    temp['法定代表人']=\
            trs[0].xpath('./td[2]').xpath('string(.)').extract_first()
    temp[trs[0].xpath('./td[3]/text()').extract_first()] =\
            trs[0].xpath('./td[4]').xpath('string(.)').extract_first()
        
    for tr in trs[1:5]:
        temp[tr.xpath('./td[1]/text()').extract_first()]=\
            tr.xpath('./td[2]').xpath('string(.)').extract_first()
        temp[tr.xpath('./td[3]/text()').extract_first()] =\
            tr.xpath('./td[4]').xpath('string(.)').extract_first()
    temp[trs[5].xpath('./td[1]/text()').extract_first()] = \
        trs[5].xpath('./td[2]/span/text()').extract_first()
    
    temp[trs[6].xpath('./td[1]/text()').extract_first()]=\
        trs[6].xpath('./td[2]').xpath('string(.)').extract_first()
    temp[trs[6].xpath('./td[3]/text()').extract_first()] =\
        trs[6].xpath('./td[4]').xpath('string(.)').extract_first()
    temp[trs[6].xpath('./td[5]/text()').extract_first()] =\
        trs[6].xpath('./td[6]').xpath('string(.)').extract_first()

    detail = trs[10].xpath('./td[2]/span/text()').extract_first()
    temp['经营范围']=detail.strip('.')
    return temp
