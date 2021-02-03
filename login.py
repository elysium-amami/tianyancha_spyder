import os, json, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def login():
    # chrome无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # path='/home/lyg/chromedriver_linux64/chromedriver'
    # driver=webdriver.Chrome(path,chrome_options=chrome_options)
    driver=webdriver.Chrome()

    # 登录
    driver.get('https://www.tianyancha.com/login')
    
    # 定位密码登录标签
    login_button = driver.find_element_by_xpath('//*[@id="web-content"]/div/div[2]/div/div/div[3]/div[3]/div[1]/div[2]')
    login_button.click()
    
    # 输入手机号
    phone=driver.find_element_by_xpath('//*[@id="mobile"]')
    phone.send_keys('17727984979')
    
    # 输入密码
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('lq118083')
    
    ensure = driver.find_element_by_xpath('//*[@id="web-content"]/div/div[2]/div/div/div[3]/div[3]/div[2]/div[4]')
    ensure.click()
    return driver
