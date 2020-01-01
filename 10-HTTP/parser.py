from collections import Counter
from bs4 import BeautifulSoup
import requests

cookie = {
    "PHPSESS": 'mn4ge5bemc2ai2dous8bf6jtgb9fra9a',
    "_ga": 'GA1.2.295525652.1577725456',
    "_gat_gtag_UA_28292940_1": "1",
    "_gid": 'GA1.2.1577002836.1577725456',
    "_vA3": '89-u--A-P19R-_79R.19-w-A-A-P19R-e_9R.p9-u--A-P19R-g_9R.\
_9-w-C-C-N19R-a49R.r9-u--A-P19R-g_9R.F0-w-C-C-H19R-W49R.N0-w-C-C-K19R\
-Y49R.58-w-A-A-Q19R-g_9R.M0-w-A-A-K19R-Q_9R.W0-w-A-A-K19R-e_9R.u9-w-A\
-A-z49R-2C0R.J0-w-A-A-H19R-Q_9R.6bY5mG',
    "_ym_d": '1577725456',
    "_ym_isad": '1',
    "_ym_uid": '1577725456510069841',
    "_ym_visorc_174977": "b",
    "autohide_news": '0',
    "bs": 'I1',
    "fps": 'd083147eb39f71e5856f3b69371c03520d',
    "is_scrollmode": '1',
    "la": "1",
    "nps7s": '2149500168',
    "pcid": 'gdhjaTQENv2',
    "pkbRem": '%7B%22uid%22%3A3036292%2C%22username%22%3A%22AntnvSrg%22\
%2C%22rem%22%3A%221ff872f0daf419dbf8e8ee0144303c6d%22%2C%22tries%22%3A0%7D',
    "pkb_modern": '11',
    "set_autohide_news": '-1',
    "spua_c6bff6": '%5B0%5D',
    "ulfs": '1577738475',
    "vn": 'eJwlyskRADEIA8GE9qMDMPknZsy+WtRQEAP+Cgqpnjheaa5O6O/o7erYnl4xc\
2ST76ZP5XPedAGMChLw',
    "ycm": '2',
}

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://pikabu.ru",
        "Connection": "keep-alive"
    }

session = requests.Session()

pages = []
for n in range(1, 11):
    pages.append(session.get(f'https://pikabu.ru/new/\
subs?of=v2&page={n}&_=1577915701765', headers=HEADERS, cookies=cookie).text)

list_of_tags = []
for page in pages:
    soup = BeautifulSoup(page, 'html.parser')
    articles = soup.find_all('article', limit=10)
    for art in articles:
        tags = art.find_all('a', {'class': 'tags__tag', "data-tag": True})
        for tag in tags:
            word = tag.get('data-tag')
            list_of_tags.append(word)

count_tags = len(list_of_tags)
top_tags = Counter(list_of_tags).most_common(10)

with open('top_tags.txt', 'w') as file:
    file.write('top 10 tags:\n\n')
    for tag in top_tags:
        file.write(f"{tag[0]} - {tag[1]}\n")
    file.write(f"\nTotal tags: {count_tags}")
