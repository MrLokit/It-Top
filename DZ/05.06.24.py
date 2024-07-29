import requests
from bs4 import BeautifulSoup

class Text:
    def __init__(self, source, title):
        self.source = source
        self.title = title

    def __str__(self):
        return f"Source: {self.source}, Title: {self.title}"

def parse_text(url, source):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items_class_1 = soup.find_all('ф', class_='ytp-title-link yt-uix-sessionlink')
    items_class_2 = soup.find_all('h1', class_='wp-block-heading')

    text_list = []
    for item in items_class_1:
        title = item.text
        text = Text(source, title)
        text_list.append(text)
    for item in items_class_2:
        title = item.text
        text = Text(source, title)
        text_list.append(text)
    return text_list

urls = [
    {'url': 'https://ru.wordpress.org/', 'source': 'Site 1'},
    {'url': 'https://wordpress.com/ru/', 'source': 'Site 2'}
]

all_text = []
for url in urls:
    all_text.extend(parse_text(url['url'], url['source']))

for text in all_text:
    print(text)
