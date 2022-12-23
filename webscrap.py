import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.flipkart.com/search?q=laptop&marketplace=FLIPKART&as-show=on&pageUID=1671710076643'
response= requests.get(url)

# Product name
product_name = []
prices = []
ratings= []

soup= BeautifulSoup(response.content, 'html')
name=soup.find_all('div', {'class': '_4rR01T'})
price= soup.find_all('div', {'class': '_30jeq3 _1_WHN1'})
rating= soup.find_all('div', {'class': '_3LWZlK'})
# print(name)
for p_name in name:
   product_name.append(p_name.text)

for p_price in price:
   prices.append(p_price.text)

for p_rating in rating:
   ratings.append(p_rating.text)

# print(len(product_name))
# print(len(prices))
# print(len(ratings))
df = pd.DataFrame({'Product Name':product_name,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
# print(product_name)
# print(prices)
# print(ratings)





# driver = webdriver.Chrome("/home/shipgig/Downloads/chromedriver_linux64")
# driver = webdriver.Chrome("/home/shipgig/Downloads/chromedriver_linux64")



# web scraping link
# driver.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

# code for getting data
# content= driver.page_source
# soup= BeautifulSoup(content)

# for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}):
#    product_name= a.find('a', href=True, attrs={'class':'_4rR01T'})

