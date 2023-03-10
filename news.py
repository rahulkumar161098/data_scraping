import pandas as pd
import requests
from bs4 import BeautifulSoup

# enter base url here
# base_url='https://www.aajtak.in/lifestyle'
base_url = 'https://zeenews.india.com/'

# storing data
title_links= []
news_title_headings= []
news_date= []
news_content= []
news_images= []

   
page= requests.get(base_url)
soup= BeautifulSoup(page.content, 'html.parser')
# print(page.reponse)
title= soup.find_all('div', attrs={'no-classs'})

for t in title: 
   a= soup.find_all('div', attrs={'class', 'story_news_description'})
   for link in a:
      link1= link.find_all('a')
      # getting link of heading
      for href in link1:
         a_link=href.get('href')
         # print(a_link)
         title_links.append(a_link)

# print(title_links)

# creating urls from base url
for url in title_links:
   created_url= base_url+str(url)
   print(created_url)
   page= requests.get(created_url)
   soup= BeautifulSoup(page.content, 'html.parser')

   # getting news headings
   title_heading= soup.find('div', attrs={'class', 'article_content'})
   # title_txt= title_heading.text
   news_title_headings.append(title_heading.text)

   # getting Time, Date and Author
   date_time= soup.find ('div', attrs={'class', 'articleauthor_details'}) 
   date_time_author= date_time.text
   get_date_time= date_time_author.split(':')[2]
   news_date.append(get_date_time)
   # print(get_date_time)

   # getting news content
   content= soup.find_all('p')
   for data in content:
      cont= data.text
      news_content.append(cont)
   
   # storing image link/download
   news_image= soup.select('div.article_image')
   news_image_link= [x.find('img') for x in news_image]
   data_source= [imgs['data-src'] for imgs in news_image_link]
   news_images.append(data_source)
   # print(data_source)


print(title_links)
print(news_title_headings)
print(news_date)
print(news_content)
print(news_images)


# print(title_headings)

# for i in titles:
#    l=i.get('href')
#    print(l)
   # for title_line in a:
   #    title_text= link.find_all('title')
   #    title_word.append(title_text)
# print(titles)
# print(title_word)

# df = pd.DataFrame({'Title':titles }) 
# df.to_csv('New data.csv', index=False, encoding='utf-8')