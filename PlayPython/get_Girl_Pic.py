import requests
from bs4 import BeautifulSoup
import os
import time

class mzitu():
    def all_url(self, url):
        html = self.request(url)
        html.encoding='utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        all_a = soup.find_all('span', class_='title')
        del(all_a[0])
        for a in all_a:
            soup = BeautifulSoup(str(a), 'lxml')
            title = soup.get_text()
            print('开始保存：',title)
            path = str(title).replace('?', '_')
            self.mkdir(path)
            href = soup.a['href']
            print(href)
            self.html(href)

    def html(self, href):   ##获得图片的页面地址
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='page').find_all('a')[-2].get_text()
        #这个上面有提到
        for page in range(1, int(max_span)):
            page_url = href + '/' + str(page)
            self.img(page_url) ##调用img函数

    def img(self, page_url): ##处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='content').find('img')['src']
        self.save(img_url)

    def save(self, img_url): ##保存图片
        name = img_url[-9:-4].replace('/','a')
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path): ##创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("C:\mzitu2", path))
        if not isExists:
            print('建了一个名字叫做', path, '的文件夹！')
            os.makedirs(os.path.join("C:\mzitu2", path))
            os.chdir(os.path.join("C:\mzitu2", path)) ##切换到目录
            return True
        else:
            print( path, '文件夹已经存在了！')
            return False

    def request(self, url): ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'referer':'http://www.mmjpg.com/tag/liufeier'
        }
        content = requests.get(url, headers=headers)
        time.sleep(1)
        return content

if __name__ == '__main__':
    Mzitu = mzitu()
    Mzitu.all_url('http://www.mmjpg.com/tag/liufeier')
