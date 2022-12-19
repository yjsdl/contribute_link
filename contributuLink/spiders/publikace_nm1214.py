# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 15:53
# @Author  : crab-pc
# @File    : publikace_nm1214.py
import re
from urllib.parse import urljoin

from Yjsdl import Spider, item


class PublikaceNm1214(Spider):
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
            url='https://publikace.nm.cz/periodicke-publikace',
            headers=self.headers.copy()
        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//div[@class="eventList eventList--pbl"]/article')
        for one in lists:
            name = one.xpath('.//div/div/a/@title')[0]
            link = one.xpath('.//div/div/a/@href')[0]
            url = urljoin('https://publikace.nm.cz', link)
            pic = one.xpath('.//div/div/a/img/@src')[0]
            meta = dict(name=name, url=url, pic=pic)
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
        issns = res.xpath('//div[@class="perex"]/text()')
        issns = ''.join(issns)
        issn = re.findall('\d+-\d+', issns)
        issns_dict = {f'issn{index + 1}': issn for index, issn in enumerate(issn)}

        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接',
                            filename='publikace_nm1214')
        data.append(dict(title_name=meta['name'], url=meta['url'], pic=meta['pic'], issn1=issns_dict.get('issn1', ''),
                         issns2=issns_dict.get('issn2', ''), contribute_link=''))
        yield data


if __name__ == '__main__':
    PublikaceNm1214.start()
