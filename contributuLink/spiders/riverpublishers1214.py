# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 13:34
# @Author  : crab-pc
# @File    : riverpublishers1214.py
from urllib.parse import urljoin
import re
from Yjsdl import Spider, item


class Riverpublishers1214(Spider):
    request_config = {
        "RETRIES": 3,
        "DELAY": 0,
        "TIMEOUT": 20
    }
    # 并发
    concurrency = 2

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    async def start_requests(self):
        yield self.request(
            url='https://www.riverpublishers.com/journals_discontinued.php',
            headers = self.headers.copy()

        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//div[@class="JLOpenBox"]')
        for one in lists:
            name = one.xpath('.//div/h2/b/a/font/text()')[0]
            url = one.xpath('.//div/h2/b/a/@href')[0]

            pic = one.xpath('.//div/a/img/@src')[0]
            pic = urljoin('https://www.riverpublishers.com', pic)

            issns = one.xpath('.//div/p//text()')
            issns = ''.join(issns)
            issn = re.findall('\d+-\d+', issns)
            issns_dict = {f'issn{index + 1}': v for index, v in enumerate(issn)}

            data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接',
                                filename='riverpublishers1214')
            data.append(
                dict(title_name=name, url=url, pic=pic, issn1=issns_dict.get('issn1', ''),
                     issn2=issns_dict.get('issn2', ''), contribute_link=''))
            yield data


if __name__ == '__main__':
    Riverpublishers1214.start()
