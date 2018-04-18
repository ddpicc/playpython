from selenium import webdriver
import time
import os
def get_cookie_from_network(url_login):
    url_login = 'https://www.douban.com/login' 
    driver = webdriver.Edge()
    time.sleep(3)
    driver.get(url_login)
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('cuiqian1988@gmail.com') # 改成你的微博账号
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('cnaiq1988') # 改成你的微博密码
    driver.find_element_by_xpath('//input[@type="submit"]').click() # 点击登录
    time.sleep(3)
    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    f = open(url_login.split('.')[1] + '_cookie.txt', 'w')
    for item in cookie_list:
        f.write(item['name'] + '=' + item['value'] + ';')
    f.seek(-1 ,os.SEEK_END)
    if f.next() == ';':
        f.seek(-1 ,os.SEEK_END)
        f.truncate()

driver.close()
