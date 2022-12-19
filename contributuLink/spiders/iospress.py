# -*- coding: utf-8 -*-
# @Time    : 2022/12/08 13:16
# @Author  : crab-pc
# @File    : iospress.py
from urllib.parse import urljoin
import pandas as pd
from Yjsdl import Spider, item


class Iospress(Spider):
    request_config = {
        "RETRIES": 3,
        "DELAY": 0,
        "TIMEOUT": 20
    }
    # 并发
    concurrency = 2

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }

    async def start_requests(self):
        for i in range(0, 8):
            yield self.request(
                # url='https://www.iospress.com/catalog?f%5B0%5D=type%3Ajournal',
                url=f'https://www.iospress.com/catalog?f%5B0%5D=type%3Ajournal&page={i}',
                headers=self.headers.copy()

            )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        all_lists = res.xpath('//div[@class="content"]/div/h2/a')
        for str1 in all_lists:
            url = str1.xpath('.//@href')[0]
            title_name = str1.xpath('.//text()')[0]
            title_name.replace('\n', '').strip()
            url = urljoin('https://www.iospress.com', url)
            # pf = pd.read_csv(r"F:\mysubject\contribute_link\contributuLink\投稿链接\iospress.csv", dtype=str).fillna('')[
            #     'url'].values.tolist()
            # if url not in pf:
            meta = dict(url=url, title_name=title_name)
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
        # 图片地址
        pic = res.xpath('//article[@class="media media--type-image media--view-mode-cover-image"]/div/img/@src')
        pic = ''.join(pic)
        # issn
        issn = res.xpath(
            '//div[@class="layout__sidebar__row layout__sidebar__row--primary layout__sidebar__row--main layout__sidebar__row--main--primary"]/div//text()')
        issn = [i.replace('\n', '').replace(' ', '') for i in issn if i != '']

        try:
            str1 = issn.index('ISSNprint')
            issn1 = issn[str1 + 1]
        except:
            issn1 = ''
        try:
            str2 = issn.index('ISSNonline')
            issn2 = issn[str2 + 1]
        except:
            issn2 = ''

        # contribute
        contribute_link = res.xpath('//div[@id="author-guidelines"]/div/div//text()')
        contribute_link = ''.join(contribute_link)
        contribute_link.replace('\n', '')

        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='iospress')
        data.append(
            dict(title_name=meta['title_name'], url=meta['url'], pic=pic, issn1=issn1, issn2=issn2))
        yield data


if __name__ == '__main__':
    Iospress.start()
