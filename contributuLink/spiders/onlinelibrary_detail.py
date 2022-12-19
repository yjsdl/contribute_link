# -*- coding: utf-8 -*-
# @date：2022/12/12 9:55
# @Author：crab-pc
# @file： onlinelibrary_detail
import random
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
    pf = pd.read_excel(r'F:\mysubject\contribute_link\contributuLink\spiders\onlinelibrary详情页.xlsx', dtype=str)
    sha = pf.shape[0]
    for i in range(8, 10):
        url = pf.values[i][0]
        # input('=====')
        # input(f'waiting---------{i}')
        browser.get(url)
        # time.sleep(random.randint(4, 6))
        html = browser.page_source
        res = etree.HTML(html)
        link = res.xpath('//a[contains(text(), "Submit an article")]/@href | //a[contains(text(), "Submit an Article")]/@href')[0] if res.xpath('//a[contains(text(), "Submit an article")]/@href | //a[contains(text(), "Submit an Article")]/@href') else ''
        data = []
        links = ''
        if link and 'http' not in link:
            links = urljoin(url, link)
        print(url, link)
        data.append(dict(url=url, contribute_link=links, contribute_links=link))
        save_list(data, 'onlinelibrary456.csv', data[0].keys())



if __name__ == '__main__':
    # first_requests()
    pf = pd.read_excel(r'F:\mysubject\contribute_link\contributuLink\spiders\onlinelibrary详情页.xlsx', dtype=str)
    pf.to_csv(r'F:\mysubject\contribute_link\contributuLink\spiders\onlinelibrary详情页.csv', index=False,encoding='utf-8')