import re
import requests
import codecs
import time
import random
from bs4 import BeautifulSoup
absolute = 'https://movie.douban.com/subject/26322642/comments'
absolute_url = 'https://movie.douban.com/subject/26322642/comments?start=23&limit=20&sort=new_score&status=P&percent_type='
url = 'https://movie.douban.com/subject/26322642/comments?start={}&limit=20&sort=new_score&status=P'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
def get_data(html):
    try:
        soup=BeautifulSoup(html,'lxml')
        comment_list = soup.select('.comment > p')
        next_page= soup.select('#paginator > a')[2].get('href')
        date_nodes = soup.select('..comment-time')
    except IndexError:
        print("index error")
    else:
        return comment_list,next_page,date_nodes

""" def get_cookie_from_network():
    from selenium import webdriver
    url_login = 'https://www.douban.com/login' 
    driver = webdriver.PhantomJS()
    driver.get(url_login)
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('cuiqian1988@gmail.com') # 改成你的微博账号
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('cnaiq1988') # 改成你的微博密码

    driver.find_element_by_xpath('//input[@type="submit"]').click() # 点击登录

    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    print(cookie_list)

    cookie_dict = {}
    for cookie in cookie_list:
        #写入文件
        f = open(cookie['name']+'.weibo','w')
        pickle.dump(cookie, f)
        f.close()

        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']

    return cookie_dict
 """
if __name__ == '__main__':
    #get_cookie_from_network()
    f_cookies = open('C:\\Users\\qcui1\\Documents\\coding\\PlayPython\\cookie.txt', 'r')
    cookies = {}
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    html = requests.get(absolute_url, cookies=cookies, headers=header).content
    comment_list = []
    # 获取评论
    comment_list, next_page,date_nodes= get_data(html,)
    soup = BeautifulSoup(html, 'lxml')
    comment_list = []
    while (next_page != []):  #查看“下一页”的A标签链接
        print(absolute + next_page)
        html = requests.get(absolute + next_page, cookies=cookies, headers=header).content
        soup = BeautifulSoup(html, 'lxml')
        comment_list, next_page,date_nodes = get_data(html)
        with open("comments.txt", 'a', encoding='utf-8')as f:
            for node in comment_list:
                comment = node.get_text().strip().replace("\n", "")
                for dateNode in date_nodes:
                    date= dateNode.get_text().strip()
                f.writelines([comment,date,u'\n'])
        time.sleep(1 + float(random.randint(1, 100)) / 20)