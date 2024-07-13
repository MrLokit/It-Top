import requests
from bs4 import BeautifulSoup
import csv

url = 'https://ru.wordpress.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

data = []
items = soup.find_all('a', class_='wp-block-button__link wp-element-button')
for item in items:
    data.append(item.text)

with open('csv04_06_24.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for item in data:
        writer.writerow([item])
