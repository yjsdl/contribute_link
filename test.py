# -*- coding: utf-8 -*-
# @date：2022/12/8 10:52
# @Author：crab-pc
# @file： test
import re

text = """
The African Journal of International and Comparative Law welcomes articles on public or private international law, either in English or French, and which have not been submitted for publication elsewhere. Articles should not exceed 12,000 words. A submission of less than 4,000 words may be considered for our shorter article Section. Papers should be typed, double spaced on one side only of A4 paper, and should be submitted in an IBM-PC and/or an Apple MAC diskette or by email. Footnotes should be numbered consecutively throughout the article and typed double spaced on a separate page.

Send submissions to:

Professor Kofi Oteng Kufuor
School of Law and Social Sciences
University of East London
University Square
1 Salway Place
Stratford, London
E15 1NF
UK

Email: K.O.Kufuor@uel.ac.uk

Note: please do not send submissions from Yahoo email accounts as these may be blocked.
"""
email=re.compile(r'[a-z0-9\-\.]+@[0-9a-z\-\.]+')
aaa = re.search(email, text)
print(aaa.group())


import httpx
import asyncio

import requests
import json

url = "https://datauthor.com/api/Media/SearchMediaByLinq"

payload = json.dumps({
  "key1": "",
  "key2": "",
  "key3": "",
  "condition1": "",
  "condition2": "",
  "field1": "PeriodName",
  "field2": "PeriodName",
  "field3": "PeriodName",
  "area": "1",
  "areaZone": [],
  "classname": "管理学",
  "classcode": "C93",
  "quota": "",
  "quotaRangeMin": 0,
  "quotaRangeMax": 0,
  "language": [],
  "evaluation": [],
  "database": [],
  "pageIndex": 1,
  "pageSize": 10,
  "order": "",
  "sort": "desc",
  "filterTitle": "",
  "FilterInfo": []
})
headers = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://datauthor.com',
  'Pragma': 'no-cache',
  'Referer': 'https://datauthor.com/Search?area=1&classname=%E7%AE%A1%E7%90%86%E5%AD%A6&classcode=C93',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  'X-ClientId': 'RUFyDXg+9RosRG9frGn/bW/SA4GHOvBXn+Ids9zD3xa9YTN8woY+1avbp9LxVBG3rqBLpGg5YOfVZDCMFxMhjg==',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())

