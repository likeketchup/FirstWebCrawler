#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import requests
import random
import re

main_url = "http://www.chinacaipu.com"


def get_html(geturl):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {'User-Agent': random.choice(user_agent_list),
               'Referer': "http://www.chinacaipu.com/menu/chinacaipu", 'Connection': 'Keep-Alive'
               }
    try:
        return requests.get(geturl, headers=headers, timeout=5).content
    except:
        print('Starting using IP Agent')
        time.sleep(1)
        the_ip = get_ip()
        proxy = {'http': the_ip}
        return requests.get(geturl, headers=headers, proxies=proxy, timeout=3).content


def get_ip():
    html_file = requests.get("http://www.kuaidaili.com/free/").text
    return random.choice(re.findall(r"\d+\.\d+\.\d+\.\d", html_file))


def parse_html(gethtml):
    soup = BeautifulSoup(gethtml, 'lxml')
    download_list = soup.find("div", attrs={"class": "ss_main"}).find("ul").find_all("li")
    meal_list = []
    for im in download_list:
        meal = im.find("div", attrs={"class": "pic"}).find("img")
        meal_list.append(meal['src'])
    next_page = soup.find("a", attrs={"title": "上一页"})
    if next_page:
        return meal_list, main_url+next_page["href"]
    return meal_list, None


if __name__ == '__main__':
    url = main_url + "/menu/chinacaipu"
    count = 0
    nameOfFile = 0
    while url and count < 3:
        count += 1
        html = get_html(url)
        pic, url = parse_html(html)
        for i in pic:
            nameOfFile += 1
            f = open(str(nameOfFile)+".jpg", 'ab')

            img = get_html(i)
            f.write(img)
            f.close()
            print("hahahaha")
            time.sleep(1)
