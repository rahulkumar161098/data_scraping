import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# base_url= 'https://www.abplive.com/news/india'
base_url = 'https://www.abplive.com/news/india/page-'
# page = requests.get(base_url)
# soup = BeautifulSoup(page.content, 'html.parser')

news_page_no= []
news_links = []
all_titles = []
sub_title = []
main_news_story = []
updated_at = []
news_img_source = []
page_no_list = []

for page_no in range(1, 76):
   multi_page_url = base_url + str(page_no)
   news_page_no.append(multi_page_url)
   # print('work on page', page_no)
   # time.sleep(.5)
   print(multi_page_url)


for url in news_page_no:
   page_url = url
   url_page = requests.get(page_url)
   page_soup = BeautifulSoup(url_page.content, 'html.parser')

   news_card= page_soup.find_all('div', attrs={'class', 'other_news'})
   for i in news_card: 
      news_link= i.find('a')
      link_source= news_link.get('href')
      news_links.append(link_source)
      # time.sleep(.5)
      # print(link_source)


for link in news_links:
   get_news_link = link
   link_page = requests.get(get_news_link)
   url_soup = BeautifulSoup(link_page.content, 'html.parser')
   if link_page.status_code == 200:
         # print(get_news_link)
      sel = url_soup.select('uk-width-expand uk-position-relative')

         # get news titles
      title = url_soup.find('h1', attrs={'class', 'article-title'})
      all_titles.append(title)
         # print(title.text)

         # get news sub_titles
      # sub_title = url_soup.find('h2', attrs={'class', 'article-excerpt'})
      # sub_title.append(sub_title.text)
         # print(sub_title.text)

      # get news story
      news_story= url_soup.select('article-data _thumbBrk uk-text-break')
      news = url_soup.find_all('p')
      sub_news_story = []
      for p in news:
         sub_news_story.append(p.text)
         # print(sub_news_story)
      main_news_story.append(sub_news_story)

         # get date and time
      date_time = url_soup.find('p', attrs={'class', 'article-author'})
      if date_time is not None:
         updated_at.append(date_time.text)
      else:
         updated_at.append(date_time)
         # print(date_time.text)

         # get image source
      img_div = url_soup.find('img', attrs={'class', 'article_feature'})
         # # img_src= [i['data-src'] for i in img_div]
      if img_div is not None:
         img_src = img_div.get('data-src')
         news_img_source.append(img_src)
      else:
         news_img_source.append(img_div)
      # print(img_src)

      print('work on this link-------------', get_news_link, '\n')
      # time.sleep(.5)

      # news_title= url_soup.find('h1', attrs={'class', 'article-title '})
      # print(news_title)


   else:
      print('Error fetching page')
      # exit()

# else:
#    print('Error fetching page')
#    exit()

# news_links = []
# all_titles = []
# sub_title = []
# main_news_story = []
# updated_at = []
# news_img_source =[]
# print(main_news_story)
print('title length', len(all_titles))
# print(len(sub_title))
print('main story length', len(main_news_story))
print('date length', len(updated_at))
print('news image source length', len(news_img_source))
print('link length', len(news_links))

df = pd.DataFrame({'Title':all_titles, 'Date and Time':updated_at, 'Image Source': news_img_source, 'Story': main_news_story, }) 
df.to_csv('ZeeNewsdemo4.csv', index=False, ) 

# '''