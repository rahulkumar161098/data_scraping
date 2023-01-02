import pandas as pd
import requests
from bs4 import BeautifulSoup
# from IPython.display import clear
# import time

name_of_candidates= []
in_BHK= []
prices= []
images= []
ir=1

# Base Url
base_url='https://myneta.info/Delhi2022/candidate.php?candidate_id='

for id in range(4871,6207):
   url= base_url+str(id)
   response= requests.get(url)
   soup= BeautifulSoup(response.content, 'html.parser')
   print('Page no- ', url)

   # name=soup.find_all('h2', attrs={'class':'main-title'})
   # # print(name)
   # for n in name:
   #    print('name',n.text)
   #    # name_of_candidates.append(n.text)
   
   # localities=soup.find_all('div', attrs={'class': 'grid_9'})
   # for l in localities:
   #    print('localities',l.text)
   #    print('location')

   # party=soup.find_all('div', attrs={'class': 'grid_2 alpha'})
   # for p in party:
   #    print('party name', p.text)

   # out = {'Specialty_{}'.format(i): specialty.get_text(strip=True) for i, specialty in enumerate(soup.select("grid_2 alpha"), 1)}
   # print(out)

   # votes = soup.find("div", {"class": "grid_3 alpha"}).find_all("div", {"class": "grid_2 alpha"})[0]
   # if(votes is None):
   #    print('null')
   # else:
   #    print(votes.text)


   
      
   

# print(soup.text)
