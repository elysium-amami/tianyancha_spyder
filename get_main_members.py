import os, json, sys
def get_zhuyao(select):
    members=select.xpath('//div[@id="_container_staffCount"]/div/table/tbody/tr')
    Ltemp=[]
    for t in members:
        temp = {}
        temp['姓名']=t.xpath('./td[2]/table/tbody/tr/td[2]/a/text()').extract_first()
        temp['职位']=t.xpath('./td[3]//span/text()').extract_first()
        temp['持股比例']=t.xpath('./td[4]/text()').extract_first()
        Ltemp.append(temp)
    return Ltemp