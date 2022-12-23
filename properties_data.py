import pandas as pd
import requests
from bs4 import BeautifulSoup

owner= []
in_BHK= []
prices= []

# Base Url
base_url='https://www.makaan.com/greater-noida-residential-property/buy-property-in-greater-noida-city?page='


for i in range(1, 653):
   url= base_url+str(i)
   # print(url)
   mult_response= requests.get(url)
   soup= BeautifulSoup(mult_response.content, 'html')
   # print(soup1)
   
   # Get builder
   own1= soup.find_all('div', attrs={'class': 'second-line'})
   for woned_by in own1:
      owner.append(woned_by.text)

   # Get rooms
   rooms= soup.find_all('div', attrs={'class': 'title-line'})
   for room in rooms:
      in_BHK.append(room.text)

   # # Get prices
   price= soup.find_all('div', attrs={'data-type': 'price-link'})
   for price in price:
      prices.append(price.text)
      # print('Price of building :- ',price.text)

# df= pd.DataFrame()
df = pd.DataFrame({'Owner':owner,'Rooms set':in_BHK, 'Price':prices }) 
df.to_csv('Gr_noida_properties_details.csv', index=False, encoding='utf-8')



# print(owner)