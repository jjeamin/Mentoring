from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
print('title : ' + soup.title.string)
print('title parent : ' + soup.title.parent.name)
print('p tag : ', soup.p)
print('a tag all : ', soup.find_all('a'))
print('get text : ' + soup.get_text())

# =============================
import requests

URL = 'http://naver.com'
response = requests.get(URL)

html = response.text
header = response.headers
status = response.status_code
is_ok = response.ok

print("header : ", header)
print("status : ", status)
print("is_ok : ", is_ok)

# =============================

import requests
from bs4 import BeautifulSoup

URL = 'http://naver.com'
response = requests.get(URL)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

search_list = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

for word in search_list:
    print(word.text)