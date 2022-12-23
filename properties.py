from bs4 import BeautifulSoup
import pandas as pd
import requests

url='https://www.makaan.com/greater-noida-residential-property/buy-property-in-greater-noida-city'
response= requests.get(url)

owner= []
in_BHK= []
total_size_in_sqft= []
prices= []
price_in_sq_ft= []
many_years_old= []
const_status_of_building= []

soup= BeautifulSoup(response.content, 'html')

print('------------------------------------------------------------------')

# Get builder
own= soup.find_all('div', attrs={'class': 'second-line'})
for woned_by in own:
   owner.append(woned_by.text)
   print('Sell by :- ', woned_by.span.text)

# Get rooms
rooms= soup.find_all('div', attrs={'class': 'title-line'})
for room in rooms:
   in_BHK.append(room.text)
   print('room set in BHK :- ',room.span.text)

# # Get prices
price= soup.find_all('div', attrs={'data-type': 'price-link'})
for price in price:
   prices.append(price.text)
   print('Price of building :- ',price.text)

# # price for sq/ft
price_sq_ft= soup.find_all('td', attrs={ 'class': 'lbl rate'})
for area in price_sq_ft:
   price_in_sq_ft.append(area.text)
   print('Price per sq/ft :- ',area.text)

# # Area in sq ft
total_sq_ft= soup.find_all('td', attrs={'class': 'size'})
for t_area in total_sq_ft:
   total_size_in_sqft.append(t_area.text)
   print('Total area in sq ft :- ', t_area.text)

# # Years old 
year_old= soup.find_all('li', attrs={'title': 'old'})
for old in year_old:
   many_years_old.append(old.text)
   print('how many years old :- ', old.text)

# Construction Status
const_status= soup.find_all('td', attrs={'class': 'val'})
for build_status in const_status:
   const_status_of_building.append(build_status.text)
   # print('Construction Status :- ', const_status.text)



# print('owner :- ', owner)

print('------------------------------------------------------------------')

# df= pd.DataFrame()
df = pd.DataFrame({'Owner':owner,'Rooms set':in_BHK, 'Price in sq ft':price_in_sq_ft, 'Total sq ft':total_size_in_sqft, 'Price':prices, 'Construction Status': const_status_of_building}) 
df.to_csv('Gr_noida_apartment.csv', index=False, encoding='utf-8')