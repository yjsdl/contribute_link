# -*- coding: utf-8 -*-
# @Time    : 2022/12/08 09:03
# @Author  : crab-pc
# @File    : thieme.py
from urllib.parse import urljoin

from Yjsdl import Spider, item


class Thieme(Spider):
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
        yield self.request(
            url='https://www.thieme.de/de/thieme-journals-470.htm',
            headers=self.headers.copy(),
        )

    async def parse(self, response):
        html = await response.text()
        res = response.html_etree(html=html)
        links = res.xpath(
            '//a[contains(text(), "Information for Advertisers") or contains(text(), "Information for advertisers")]/@href')
        i = 9
        for one in links[0:1]:
            if not one.endswith('.pdf'):
                one = '/de/thoracic-cardiovascular-surgeon/advertisers-6866.htm'
                url = urljoin('https://www.thieme.de', one)
                meta = dict(url=url)
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
        # 作者链接
        authors = res.xpath('//a[text()="Authors"]/@href')
        authors = ''.join(authors)
        # 标题
        title_name = res.xpath('//div[@id="header-title"]/span/text()')
        title_name = ''.join(title_name)
        # 图片链接
        pic = res.xpath('//p[@class="teaser-img"]/img/@src')
        pic = ''.join(pic)
        pic = urljoin('https://www.thieme.de', pic)
        #issn
        issn = res.xpath('//h2[contains(text(), "Bibliographic Data")]/../table/tbody/tr/td//text()')
        issn = ''.join(issn)

        meta_copy = dict(title_name=title_name, url=meta['url'], pic=pic, issn=issn)
        url = urljoin('https://www.thieme.de', authors)
        yield self.request(
            url=url,
            headers=self.headers.copy(),
            meta=meta_copy,
            callback=self.get_headlink
        )

    async def get_headlink(self, response):
        meta = response.meta
        html = await response.text()
        res = response.html_etree(html=html)
        link = res.xpath('//span[contains(text(), "Submit your research here")]/../@href')
        contribute_link = ''.join(link)
        aaa = dict(contribute_link=contribute_link)
        meta.update(aaa.copy())
        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接', filename='thieme')
        data.append(meta)
        yield data



if __name__ == '__main__':
    Thieme.start()
