# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 15:53
# @Author  : crab-pc
# @File    : editorial.py
from urllib.parse import urljoin

from Yjsdl import Spider, item


class Editorial(Spider):
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
    aiohttp_kwargs = {'proxy': 'http://127.0.0.1:1080'}

    async def start_requests(self):
        yield self.request(
            url='https://editorial.us.es/es/revistas',
            headers=self.headers.copy()
        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//div[@class="views-field views-field-title"]')
        for one in lists[1:]:
            name = one.xpath('.//span/a/text()')[0]
            link = one.xpath('.//span/a/@href')[0]
            url = urljoin('https://editorial.us.es', link)
            meta = dict(title_name=name, url=url)
            yield self.request(
                url=url,
                headers=self.headers.copy(),
                meta=meta,
                callback=self.detail_parse
            )

    async def detail_parse(self, response):
        meta = response.meta
        html = await response.text()
        res = response.html_etree(html=html)
        pic = res.xpath('//div[@class="field-item even"]/img/@src')[0] if res.xpath(
            '//div[@class="field-item even"]/img/@src') else ''
        msg = res.xpath('//div[@class="group-contenido-texto field-group-div flexItem"]//text()')
        msg = [i.replace(':\xa0', '') for i in msg]
        try:
            issn = msg[msg.index('ISSN') + 1]
        except:
            issn = ''
        try:
            eissn = msg[msg.index('e-ISSN') + 1]
        except:
            eissn = ''
        try:
            doi = msg[msg.index('Nº DOI') + 1]
        except:
            doi = ''
        try:
            email = msg[msg.index('Correo') + 1]
        except:
            email = ''
        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='editorial')
        data.append(dict(title_name=meta['title_name'], url=meta['url'], pic=pic, issn1=issn, issn2=eissn, doi=doi, email=email))
        yield data


if __name__ == '__main__':
    Editorial.start()
