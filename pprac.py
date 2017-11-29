#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Programmed by Toma

from bs4 import BeautifulSoup
import codecs
import requests

download_url = "http://blog.jobbole.com/29281"


def __init__(self):
    self.__name = "toma"
    self.__personality = "kind"


def get_html(download_url):
    return requests.get(download_url).content


def parse_url(html_file):
    soup = BeautifulSoup(html_file,'lxml')
    tag_list = soup.find("ol").find_all("li")
    link_list = []
    for link in tag_list:
        link_list.append(link.find("a"))
    return link_list


def main():
    for i in parse_url(get_html(download_url)):
        print(i["href"], "\n")


if __name__ == '__main__':
    main()