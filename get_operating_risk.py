import os, json, sys
import scrapy


def get_operating_risk(select):
    temp = {}
    temp['股权出质'] = select.xpath('//*[@id="nav-main-equityCount"]/span[2]/text()').extract_first()

    try:
        temp['历史股权出质'] = select.xpath('//*[@id="nav-main-equityCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史股权出质'] = None

    temp['行政处罚'] = select.xpath('//*[@id="nav-main-punishmentV2"]/span[2]/text()').extract_first()

    try:
        temp['历史行政处罚'] = select.xpath(
            '//*[@id="nav-main-punishmentV2"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史行政处罚'] = None

    temp['经营异常'] = select.xpath('//*[@id="nav-main-abnormalCount"]/span[2]/text()').extract_first()

    try:
        temp['历史经营异常'] = select.xpath(
            '//*[@id="nav-main-abnormalCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史经营异常'] = None

    temp['股权质押'] = select.xpath('//*[@id="nav-main-equityPledgeTotalCount"]/span[2]/text()').extract_first()

    try:
        temp['历史股权质押'] = select.xpath(
            '//*[@id="nav-main-equityPledgeTotalCount"]/span[3]/span[2]/text()').extract_first()
    except:
        temp['历史股权质押'] = None

    return temp