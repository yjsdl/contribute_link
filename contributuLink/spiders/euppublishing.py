# -*- coding: utf-8 -*-
# @Time    : 2022/12/08 11:11
# @Author  : crab-pc
# @File    : euppublishing.py
from urllib.parse import urljoin

from Yjsdl import Spider,item


class Euppublishing(Spider):
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
        for i in range(0, 3):
            yield self.request(
                url=f'https://www.euppublishing.com/action/showPublications?startPage={i}',
                headers=self.headers.copy()
            )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        all_lists = res.xpath('//div[@class="contentRow"]')

        for one in all_lists:
            aaa = dict()
            title_name = one.xpath('.//div[@class="pubTitle"]/a/text()')[0]
            bbb = one.xpath('.//div//text()')
            bbb = [i.replace('\n', '').replace(' ', '') for i in bbb if i != '']
            for str1 in bbb:
                str2 = str1.split(':')
                if len(str2) >= 2:
                    aaa[str2[0]] = str2[1]


            url = one.xpath('.//div[@class="pubTitle"]/a/@href')[0]
            url = urljoin('https://www.euppublishing.com', url)
            ccc = url.rsplit('/', maxsplit=1)[1]
            url = f'https://www.euppublishing.com/page/{ccc}/submissions'

            pic = one.xpath('.//div[@class="imageContainer"]/a/img/@src')[0]
            pic = urljoin('https://www.euppublishing.com', pic)
            issn1 = aaa.get('ISSN')
            issn2 = aaa.get('eISSN')

            data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='euppublishing')
            data.append(dict(title_name=title_name, url=url, pic=pic, issn1=issn1, issn2=issn2))
            yield data


if __name__ == '__main__':
    Euppublishing.start()
