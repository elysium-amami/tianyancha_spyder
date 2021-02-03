import os, json, sys
import scrapy
def get_judicial_risk(select):
    temp = {}
    temp['开庭公告'] = select.xpath('//*[@id="nav-main-announcementCount"]/span[2]/text()').extract_first()
    
    try:
        temp['历史开庭公告'] = select.xpath('//*[@id="nav-main-announcementCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史开庭公告'] = None
        
    temp['法律诉讼'] = select.xpath('//*[@id="nav-main-lawsuitWithLabelCount"]/span[2]/text()').extract_first()
    
    try:
        temp['历史法律诉讼'] = select.xpath('//*[@id="nav-main-lawsuitWithLabelCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史法律诉讼'] = None
        
    temp['法院公告'] = select.xpath('//*[@id="nav-main-courtCount"]/span[2]/text()').extract_first()

    try:
        temp['历史法院公告'] = select.xpath('//*[@id="nav-main-courtCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史法院公告'] = None

    temp['司法协助'] = select.xpath('//*[@id="nav-main-judicialaAidCount"]/span[2]/text()').extract_first()
    
    try:
        temp['历史司法协助'] = select.xpath('//*[@id="nav-main-judicialaAidCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史司法协助'] = None
        
    temp['立案信息'] = select.xpath('//*[@id="nav-main-courtRegisterCount"]/span[2]/text()').extract_first()

    try:
        temp['历史立案信息'] = select.xpath('//*[@id="nav-main-courtRegisterCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史立案信息'] = None

    temp['破产重整'] = select.xpath('//*[@id="nav-main-bankruptcyCount"]/span[2]/text()').extract_first()

    try:
        temp['历史破产重整'] = select.xpath('//*[@id="nav-main-bankruptcyCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史破产重整'] = None

    return temp