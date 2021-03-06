import requests
from bs4 import BeautifulSoup

BASE_URLS = 'https://vnexpress.net/{}'

# BASE_URLS = 'https://vnexpress.net/so-hoa/cong-nghe'
# BASE_URLS = 'https://vnexpress.net/thoi-su'
# page = requests.get(BASE_URLS)


def article_news(page):
  list_articles = []

  soup = BeautifulSoup(page.content, 'html.parser')
  articles = soup.find_all('article')

  for article in articles:
    try:
      img = article.find_all(class_='lazy')[0].get('data-src') or article.find_all(class_='lazy')[0].get('src')
      title = article.find_all(class_='title-news')[0].text
      description = article.find_all(class_='description')[0].text 
    except IndexError:
      continue

    tuple_article = (img, title, description,)
    list_articles.append(tuple_article)
  
  return list_articles


def news():
  page = requests.get(BASE_URLS.format('thoi-su'))
  return article_news(page)


def business_news():
  page = requests.get(BASE_URLS.format('kinh-doanh'))
  return article_news(page)


def technology_news():
  page = requests.get(BASE_URLS.format('so-hoa/cong-nghe'))
  return article_news(page)
