#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Programmed by Toma Chen
# 羊肉串涮火锅麻辣烫
# 轮子
from bs4 import BeautifulSoup
import requests
import codecs

download_url = "http://movie.douban.com/top250"


def __init__(self):
    self.name = "toma"
    self.personality = "kind"
    pass


def main():
    url = download_url
    with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KH'
                      'TML, like Gecko)'
    }
    return requests.get(url, headers=headers).content


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'bd'})
        movie_name = detail.find('span', attrs={'class': 'inq'}).getText()
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, download_url + next_page['href']
    return movie_name_list, None


if __name__ == '__main__':
    main()


'''


queue = deque()
visited = set()
url = "http://news.dbanotes.net"
queue.append(url)
cnt = 0
while queue:
    url = queue.popleft()  # 队首元素滚蛋
    visited |= {url}  # 加入已访问清单
    print("已经抓取" + str(cnt) + "正在爬取" + url)  # 输出爬取状态
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if "html" not in urlop.getheader("Content-Type"):
        continue

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('Add in the queue --->  ' + x)
word ={}
word["name"] = "toma"
word = urllib.parse.urlencode(word)
url = "https://www.baidu.com/baidu?wd="
full_url = url+word
print(full_url)
data = urllib.request.urlopen(full_url).read()
data = data.decode("UTF-8")
print(data)

'''