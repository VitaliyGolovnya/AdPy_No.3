import bs4
import requests

url = 'https://habr.com/ru/all'

response = requests.get(url=url)
response.raise_for_status()
text = response.text

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    for hub in hubs:
        hub_name = hub.find('span').text.lower()
        if hub_name in KEYWORDS:
            title_element = article.find('a', class_='tm-article-snippet__title-link')
            link = 'https://habr.com' + title_element.attrs.get('href')
            date = article.find('span', class_='tm-article-snippet__datetime-published').find('time')
            print(f'<{date.attrs.get("title")}> - <{title_element.text}> - <{link}>')
            break






