import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url= 'https://www.abplive.com/news/india'
page= requests.get(base_url)
soup= BeautifulSoup(page.content, 'html.parser')
news_card= soup.find_all('div', attrs={'class', 'other_news'})

news_links = []
all_titles = []
sub_title = []
main_news_story = []
updated_at = []
news_img_source =[]

if page.status_code==200:
   for i in news_card:
      news_link= i.find('a')
      link_source= news_link.get('href')
      news_links.append(link_source)

   for link in news_links:
      get_news_link= link
      link_page= requests.get(get_news_link)
      url_soup= BeautifulSoup(link_page.content, 'html.parser')
      if link_page.status_code == 200:
         # print(get_news_link)
         sel= url_soup.select('uk-width-expand uk-position-relative')

         # get news titles
         title= url_soup.find('h1', attrs={'class', 'article-title'})
         all_titles.append(title)
         # print(title.text)

         # get news sub_titles
         sub_title= url_soup.find('h2', attrs={'class', 'article-excerpt'})
         sub_title.append(sub_title.text)
         # print(sub_title.text)

         # get news story
         # news_story= url_soup.select('article-data _thumbBrk uk-text-break')
         news= url_soup.find_all('p')
         sub_news_story=[]
         for p in news:
            sub_news_story.append(p.text)
         # print(sub_news_story)
         main_news_story.append(sub_news_story)

         # get date and time
         date_time= url_soup.find('p', attrs={'class', 'article-author'})
         updated_at.append(date_time)
         # print(date_time.text)

         # get image source
         img_div= url_soup.find('img', attrs={'class', 'article_feature'})
         # img_src= [i['data-src'] for i in img_div]
         img_src= img_div.get('data-src')
         news_img_source.append(img_src)
         print(img_src)

         print('----------------------------------------------')
         # news_title= url_soup.find('h1', attrs={'class', 'article-title '})
         # print(news_title)



      else:
         print('Error fetching page')
         exit()
      


else:
   print('Error fetching page')
   exit()


# news_links = []
# all_titles = []
# sub_title = []
# main_news_story = []
# updated_at = []
# news_img_source =[]
# print(main_news_story)
print(len(all_titles))
print(len(sub_title))
print(len(main_news_story))
print(len(updated_at))
print(len(news_img_source))
# print(len())