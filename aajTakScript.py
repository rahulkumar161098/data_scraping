import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url= 'https://www.aajtak.in/elections'
page= requests.get(base_url)
soup= BeautifulSoup(page.content, 'html.parser')

news_titles= []
news_sub_titles= []
news_links= []
main_story= []
news_date_time= []
news_img_source= []

if page.status_code == 200:
	
   # getting page info
   title= soup.select('div.left-sec div.sm-thumb-listing ul li')
   # print(title)
   for t in title:
      # print(t)
      news_list= t.find('a')
      news_link= news_list.get('href')
      news_links.append(news_link)
      # news_title= news_list.get('title')

   # Fetching single single page
   for link in news_links:
      get_single_link= link
      single_page= requests.get(get_single_link)
      soup= BeautifulSoup(single_page.content, 'html.parser')

      if single_page.status_code == 200:
         # print('success')

         # Get Story Title
         story_title= soup.find('div', attrs={'class', 'story-heading'})
         # print(story_title.text)
         news_titles.append(story_title.text)

         # Get Story Sub-Title
         sub_title= soup.find('div', attrs={'class', 'sab-head-tranlate-sec'})
         # print(sub_title.text)
         news_sub_titles.append(sub_title)

         # Get News Contents
         story= soup.select('div', attrs={'class','story-with-main-sec'})
         # print(story)
         for s in story:
            p= soup.find_all('p', attrs={'class' ,'text-align-justify'})
            # print(p)
            s=[]
         for point in p:
            # print(point.text)
            s.append(point.text)
         main_story.append(s)

         # download images 
         image= soup.select('div.main-img')
         img_url= [x.find('img') for x in image]
         img_data_source= [img['data-src'] for img in img_url]
         # print(img_data_source)
         news_img_source.append(img_data_source)


         # Get Date and Time of news
         d_and_time= soup.select('div.user-detial-left ul')
         for l in d_and_time:
            li= l.find_all('li')
            date_time=[]
            for date in li:
               # print(date.text)
               date_time.append(date.text)
            # print(date_time)
            news_date_time.append(date_time)
         
      else:
         print('Error fetching page')
         exit()

      '''
      for l in news_list:
         print(l)
         # news_list.append
      print(t.get('href'))
      print(news_list)
      a= soup.find_all('a')
      print(t.text)
      for link in a:
         news_link= link.find_all('a')
         # print(news_link)
         for href in news_link:
             a_link= href.get('href')
             print(a_link)

   # for t in title:
   #       news_title.append(t.text)
   # print(title.text)
   '''

else:
	print("Error fetching page")
	exit()

df = pd.DataFrame({'Title':news_titles, 'Sub-Title': news_sub_titles, 'Image Source': news_img_source, 'Date and Time': news_date_time,'Story': main_story, }) 
df.to_csv('AajTakNews.csv', index=False, ) 
# print(news_links)
# print(news_img_source)
# print(news_date_time)
print(len(news_titles))
print(len(news_sub_titles))
print(len(main_story))
print(len(news_date_time))
print(len(news_img_source))

