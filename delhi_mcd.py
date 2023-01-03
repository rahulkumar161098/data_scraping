import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url='https://myneta.info/Delhi2022/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary'
response= requests.get(base_url)
soup= BeautifulSoup(response.content, 'html.parser')
table = soup.find_all('table')[2]
rows= table.find_all('tr')

Candidate_name=[]
Constituency=[]
Party=[]
Criminal_case=[]
Education=[]
Total_assets=[]
Liabilities=[]


for row in rows:
   cells=row.find_all('td')
   cell_text= [cell.get_text(strip=True) for cell in cells]
   # splt_text= [s_text.split("[]") for s_text in cell_text[1:2]]
   # print(cell_text[1:2])
   # print(cell_text[7:])
   Candidate_name.append(cell_text[1:2])
   Constituency.append(cell_text[2:3])
   Party.append(cell_text[3:4])
   Criminal_case.append(cell_text[4:5])
   Education.append(cell_text[5:6])
   Total_assets.append(cell_text[6:7])
   Liabilities.append(cell_text[7:])

df = pd.DataFrame({'Candidate Name':Candidate_name, 'Constituency':Constituency, 'Party':Party, 'Criminal_case': Criminal_case, 'Education': Education, 'Total_assets': Total_assets, 'Liabilities': Liabilities }) 
df.to_csv('Delhi_MCD.csv', index=False, encoding='utf-8')

# print(rows)
# t_body = table.select('tbody')
# for i in t_body.find_all('tr'):
#    print(i.text)
# print(t_body.text)
   # row= tbody.find_all('tr')
   # print(row)


# rows= table.find_all('tr')
# print(rows)

# for row in rows:
#       name= row.find_all('td')[1].text
#       print(name)
# print(name.text)
# data=[]
# for i in name.find_all('td'):
#    name=i.text
#    splt= name.split(',')
#    data.append(splt)

# # print(data)
# name= []
# for j in range(1, len(data), 6):
#    name.append(data[j])
#    data[j].append(data[j])
# print(name)



# votes = soup.find("div", {"class": "grid_3 alpha"}).find_all("div", {"class": "grid_2 alpha"})[0]
