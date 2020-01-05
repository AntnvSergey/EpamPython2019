from collections import Counter
from bs4 import BeautifulSoup
import requests

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://pikabu.ru",
        "Connection": "keep-alive"
    }

data = []
with open("cookie.txt", "r") as file:
    for line in file:
        data.append(line.split())

session = requests.Session()

pages = []
for n in range(1, 11):
    pages.append(session.get(f'https://pikabu.ru/new/\
subs?of=v2&page={n}&_=1577915701765', headers=HEADERS, cookies=dict(data)).text)

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
