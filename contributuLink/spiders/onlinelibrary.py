# -*- coding: utf-8 -*-
# @Time    : 2022/12/09 10:07
# @Author  : crab-pc
# @File    : onlinelibrary.py
from urllib.parse import urljoin
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from lxml import etree

threadpool = ThreadPoolExecutor(max_workers=2)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # 前面设置的端口号
browser = webdriver.Chrome(executable_path=r'D:\python38\chromedriver.exe',
                           options=chrome_options)  # executable执行webdriver驱动的文件


def save_list(data, file, name):
    # desk = os.path.join(os.path.expanduser('~'), 'Desktop')
    # 当前文件夹
    file_path = r'F:\mysubject\contribute_link\contributuLink\投稿链接\\' + file
    if os.path.isfile(file_path):
        df = pd.DataFrame(data=data)
        df.to_csv(file_path, encoding="utf-8", mode='a', header=False, index=False)
    else:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df = pd.DataFrame(data=data, columns=name)
        df.to_csv(file_path, encoding="utf-8", index=False)

def first_requests():
    for i in range(1, 200):
        input('=====')
        input(f'waiting---------{i}')
        html = browser.page_source
        res = etree.HTML(html)
        lists = res.xpath('//ul[@id="search-result"]/li')
        data = []
        for one in lists:
            title_name = one.xpath('.//div/h3/a/text() | .//div/span/a/text()')[0]
            url = one.xpath('.//div/h3/a/@href | .//div/span/a/@href')[0]
            url = urljoin('https://onlinelibrary.wiley.com', url)
            pic = one.xpath('.//div[@class="item__image"]/img/@src | .//a[@class="item__image"]/img/@src')[0] if one.xpath('.//div[@class="item__image"]/img/@src | .//a[@class="item__image"]/img/@src') else ''
            pic = urljoin('https://onlinelibrary.wiley.com', pic)

            issn = one.xpath('.//div/div[@class="meta__issns"]/text()')
            issn = ''.join(issn)
            try:
                issn = issn.split(': ')[1]
            except:
                issn = ''

            eissn = one.xpath('.//div/div[@class="meta__eissn"]/text()')
            eissn = ''.join(eissn)
            try:
                eissn = eissn.split(': ')[1]
            except:
                eissn = ''

            data.append(dict(title_name=title_name, url=url, pic=pic, issn=issn, eissn=eissn))
        save_list(data, 'onlinelibrary123.csv', data[0].keys())



if __name__ == '__main__':
    first_requests()
