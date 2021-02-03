import os, json, sys
import scrapy
def get_report(select):
    anaul_reports = select.xpath('//*[@id="nav-main-backgroundItem"]/div[@tyc-event-ch="CompangyDetail.nianbao"]/div[2]/div/table/tbody/tr')
    Ltemp = []
    for t in anaul_reports:
        temp = {}
        temp['企业年报'] = t.xpath('./td[2]/text()').extract_first()
        temp['年报链接'] = t.xpath('./td[3]/a/@href').extract_first()
        Ltemp.append(temp)
    return Ltemp