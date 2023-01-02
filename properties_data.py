import pandas as pd
import requests
from bs4 import BeautifulSoup
# from IPython.display import clear
# import time

owner= []
in_BHK= []
prices= []
images= []
ir=1

# Base Url
base_url='https://www.makaan.com/greater-noida-residential-property/buy-property-in-greater-noida-city?page='


for i in range(1, 640):
   url= base_url+str(i)
   # print(url)
   print('Scrapnig on page no. ',{i})
   # clear_output(wait=True)
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


   # div_tag= soup.select('div.img-slide div.gallerywrap div.img-slide')
   div_tag= soup.select('div.imgWrap figure')

   # print('div tag',(div_tag))
   # print(div_tag[0])
   # print('--------------------------------------------')
   img_url= [ x.find('img') for x in div_tag]
   # print('img_url',(img_url))
   # print(img_url[0])
   # print('--------------------------------------------')
   img_list= [ imgs['data-src'] for imgs in img_url]
   # print('--------------------------------------------')
   # for j in (0, len(img_list)-1):
   j=0
   while j< len(img_list):
      if(img_list[j].startswith('https')):
         img_list[j]=img_list[j]
      else:
         img_list[j]=f'{"https://www.makaan.com"+img_list[j]}'
      images.append(img_list[j])
      j=j+1
   # print(img_list)
   # print(img_list)

   # print('owner',len(owner))
   # print('bhk',len(in_BHK))
   # print('price',len(prices))
   # print('images',len(images))

   # for img_save in img_list:
   #    temp= requests.get(img_save)
   #    print(temp)
   #    # f= open(f'img-{ir}.png', 'wb')
   #    # image_save=f.write(temp.content)
   #    # images.append(image_save)
   #    # f.close()
   #    ir+=1

# print('images',images)
# df= pd.DataFrame()
df = pd.DataFrame({'Owner':owner,'Rooms set':in_BHK, 'Price':prices,'property_image':images }) 
df.to_csv('Gr_noida_real_estate_propertie.csv', index=False, encoding='utf-8')



# print(owner)