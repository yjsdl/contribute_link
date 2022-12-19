# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 16:41
# @Author  : crab-pc
# @File    : jomardpublishing.py
import re
from urllib.parse import urljoin

from Yjsdl import Spider, item


class Jomardpublishing(Spider):
    request_config = {
        "RETRIES": 3,
        "DELAY": 0,
        "TIMEOUT": 20
    }
    # 并发
    concurrency = 2

    aiohttp_kwargs = {'proxy': 'http://127.0.0.1:1080'}

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    async def start_requests(self):
        yield self.request(
            url='http://jomardpublishing.com/journals.aspx?lang=en',
            headers=self.headers.copy()
        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//div[@class="media"]')
        for one in lists[1:]:
            name = one.xpath('.//div/h5/a/text()')[0]
            link = one.xpath('.//div/h5/a/@href')[0]
            url = urljoin('http://jomardpublishing.com/', link)

            pic = one.xpath('.//a/img/@src')[0]
            pic = urljoin('http://jomardpublishing.com', pic)

            summary = one.xpath('.//div/p//text()')
            summary = ''.join(summary)
            issns = re.findall('\d+-\d+', summary)

            issns_dict = {f'issn{index+ 1}': issn for index, issn in enumerate(issns)}
            meta = dict(title_name=name, url=url, pic=pic, issns=issns)
            yield self.request(
                url=url,
                headers=self.headers.copy(),
                meta=meta,
                callback=self.details_parse
            )

    async def details_parse(self, response):
        meta = response.meta
        html = await response.text()
        res = response.html_etree(html=html)
        contribute_links = res.xpath('//ul[@class="side-nav"]/li/a/text()')
        index = contribute_links.index('Manuscript submission')
        contribute_link = res.xpath(f'//ul[@class="side-nav"]/li[{index + 1}]/a/@href')[0]
        contribute_link = urljoin('http://jomardpublishing.com', contribute_link)

        issns_dict = {f'issn{index + 1}': issn for index, issn in enumerate(meta.get('issns', ''))}

        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='jomardpublishing')
        data.append(dict(title_name=meta['title_name'], url=meta['url'], pic=meta['pic'], issn1=issns_dict.get('issn1', ''),
                         issn2 = issns_dict.get('issn2', ''), contribute_link=contribute_link))
        yield data

if __name__ == '__main__':
    Jomardpublishing.start()


# import requests
#
# url = "http://jomardpublishing.com/journals.aspx?lang=en"
#
# payload={}
# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cache-Control': 'no-cache',
#   'Cookie': 'ASP.NET_SessionId=ejjcvceooxzkb0whqkjf1jwg; _ga=GA1.2.810450356.1670920683; _gid=GA1.2.1104132224.1670920683; langsite=en; __atuvc=2%7C50; __atuvs=63983a4a1255f4ac001; langsite=en',
#   'Pragma': 'no-cache',
#   'Proxy-Connection': 'keep-alive',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
