# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 09:54
# @Author  : crab-pc
# @File    : journalsaps1214.py
import re
from urllib.parse import urljoin

from Yjsdl import Spider, item


class Journalsaps1214(Spider):
    request_config = {
        "RETRIES": 3,
        "DELAY": 0,
        "TIMEOUT": 20
    }
    # 并发
    concurrency = 2

    headers = {
        # 'authority': 'www.euppublishing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
    }

    async def start_requests(self):
        yield self.request(
            url='https://journals.aps.org/about',
            headers=self.headers.copy(),
        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//ul[@class="dropdown overflow"]/li')
        for one in lists[1:]:
            name = one.xpath('.//a/text()')[0]
            link = one.xpath('.//a/@href')[0]
            url = urljoin('https://journals.aps.org', link)
            meta = dict(name=name, url=url)
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
        issns = res.xpath('//p[@class="legal"]//text()')
        issns = ''.join(issns)
        issn = re.findall('\d+-\d+', issns)

        issns_dict = {f'issn{index + 1}': issn for index, issn in enumerate(issn)}
        contribute_link = 'https://authors.aps.org/Submissions/login/new'

        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='journalsaps1214')
        data.append(dict(title_name=meta['name'], url=meta['url'], issn1=issns_dict.get('issn1', ''), issns2=issns_dict.get('issn2', ''), contribute_link=contribute_link))
        yield data

if __name__ == '__main__':
    Journalsaps1214.start()
