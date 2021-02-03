import os, json, sys
import scrapy
def get_gongshang(select):
    trs = select.xpath('//*[@id="_container_baseInfo"]/table//tr')
    temp={}

    temp['法定代表人']=\
            trs[0].xpath('./td[2]').xpath('string(.)').extract_first()
    temp['经营状态'] =\
            trs[0].xpath('./td[4]').xpath('string(.)').extract_first()

    temp['成立日期'] = \
        trs[1].xpath('./td[2]').xpath('string(.)').extract_first()
    temp['注册资本'] = \
        trs[2].xpath('./td[2]').xpath('string(.)').extract_first()

    temp['实缴资本'] = \
        trs[3].xpath('./td[2]').xpath('string(.)').extract_first()
    temp['工商注册号'] = \
        trs[3].xpath('./td[4]').xpath('string(.)').extract_first()

    temp['统一社会信用代码'] = \
        trs[4].xpath('./td[2]').xpath('string(.)').extract_first()
    temp['纳税人识别号'] = \
        trs[4].xpath('./td[4]').xpath('string(.)').extract_first()

    temp['营业期限'] = \
        trs[5].xpath('./td[2]/span/text()').extract_first()

    temp['公司类型']=\
        trs[6].xpath('./td[2]').xpath('string(.)').extract_first()
    temp['行业'] =\
        trs[6].xpath('./td[4]').xpath('string(.)').extract_first()
    temp['人员规模'] =\
        trs[6].xpath('./td[6]').xpath('string(.)').extract_first()

    detail = trs[10].xpath('./td[2]/span/text()').extract_first()
    temp['经营范围']=detail.strip('.')
    return temp
