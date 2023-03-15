import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url='https://www.thelallantop.com/all/sports'
page= requests.get(base_url)
soup= BeautifulSoup(page.content, 'html.parser')

news_container= soup.select('div.news-card-box div.news-card-body div.headline-wrap div.row-modify-10 div.col')
# print(news_container)
for news_card in news_container:
   # news= soup.find('div', attrs={'class', 'series-row'})
   news= news_card.select('div.news-card-box div.news-card-body div.headline-wrap div.row-modify-10 div.col div.headline-box-sm div.headline-right-col div.headline-body div.headline-info')
   for new in news:
      a= new.get('h3')
      # label= soup.find('div', attrs={'class', 'series-row'})
      print(a)

   # for all_news in news:
   #    single_card= soup.find('div', attrs={'class', 'headline-box-sm'})
   #    label= soup.find('div', attrs={'class', 'series-row'})

   #    print(label.text)


# heading= soup.find_all('div', attrs={'class', 'content-wrapper'})
# c=0
# for i in heading:
#    print(i)