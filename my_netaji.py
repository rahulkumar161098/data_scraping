import pandas as pd
import requests
from bs4 import BeautifulSoup
# from IPython.display import clear
# import time

all_link=[]
candidate_id=[]
candidate_edu_details=[]
candidate_name=[]
candidate_party= []
candidate_age= []
so_wo= []
candidate_edu_details=[]
assets_liabilitie= []
candidate_self_professions= []
candidate_spouse_professions= []
criminal_case= []

# Base Url
base_url='https://myneta.info/Gujarat2022/index.php?action=summary&subAction=candidates_analyzed&sort=candidate#summary'

page= requests.get(base_url)
soup= BeautifulSoup(page.content, 'html.parser')
link= soup.find_all('table')[2]
rows= link.find_all('tr')




for row in rows:
   data= row.find_all('td')
   # c_link= [i['href']]
   a= row.find_all('a')    #find anchor tage in html
   all_link.append(a)
   for i in a:
      a_link=i.get('href')    #to get href link
      id=a_link.split("=")    #split by = to get id
      # print(id[1])
      candidate_id.append(id[1])
      
del candidate_id[0:7]
# print(candidate_id)
c_out=0
candidate_details_base_url='https://myneta.info/Gujarat2022/candidate.php?candidate_id='
for i in candidate_id:
   url= candidate_details_base_url+str(i)
   print('Candidate url', i)
   c_out+=1
   print(c_out)
   page_details= requests.get(url)
   # print(page_details)     #check response of url
   soup1= BeautifulSoup(page_details.content, 'html.parser')
   # print(soup1)

   name= soup1.find('h2', attrs={'class': 'main-title'})
   for n in name:
      # print(n.text)
      c_name=n.text
      candidate_name.append(n.text)
      
   other_details= soup1.find_all('div', attrs={'class': 'grid_2 alpha'})
   # for d in other_details:
      # print(d.text)
   result=[ i.text for i in other_details ]
   # print(result[0])
   candidate_party.append(result[0])
   candidate_age.append(result[2])  
   so_wo.append(result[1])



   # Getting Education details
   edu_details= soup1.find_all('div', attrs={'class': 'grid_3 alpha omega left-border-div left-blue-border'})
   e_details= [e.text for e in edu_details]
   candidate_edu_details.append(edu_details)
   # print(e_details)

   assets_liabilities=soup1.find_all('div', attrs={'class': 'bottom-border-div red fullWidth' })
   al_details= [x.text for x in assets_liabilities]
   # print(al_details)
   assets_liabilitie.append(al_details)

   
   # Getting Profession details
   professions= soup1.select('table')[7]
   p_row= professions.find_all('tr')
   # p_col= p_row.find_all('td')
   p_result= [ p.get_text('td') for p in p_row ]
   candidate_self_professions.append(p_result[1])
   candidate_spouse_professions.append(p_result[2])
   # print(p_result[1])
   # print(p_result[2])

   # Number of cases
   c_case=[]
   c_cc= []
   case= soup1.find('div', attrs={'class': 'grid_3 alpha left-border-div left-green-border'})
   # c_case= case.getText('sapn')
   # print(case.text)
   c_case.append(case.text)
   for cc in c_case:
      ccc=cc.split(':')
      criminal_case.append(ccc)
      # print(ccc)
   # print(c_case)

   # print('Candidate name :', c_name, 'Candidate Age: ',result[2], 'Candidate Party :',result[0], 'So/Wo/Do: ',result[1], 'Candidate Educations: ', e_details, 'Candidate A&L: ',al_details, 'Candidate Self Professions: ', p_result[1], 'Candidate Spouse Professions: ',p_result[2]  )

   print('------------------------------------')
   # for row['tr'] in professions:
   #    cell_row= row.find_all('td')
   #    print(cell_row)
   # pro_result= [i.find('tr') for i in professions]
   # print(pro_result)

df = pd.DataFrame({'Candidate name': candidate_name, 'Candidate Age': candidate_age, 'Candidate Party':  candidate_party, 'So/Wo/Do': so_wo, 'Candidate Educations': candidate_edu_details, 'Candidate A&L':assets_liabilitie, 'Candidate Self Professions': candidate_self_professions, 'Candidate Spouse Professions': candidate_spouse_professions, 'Candidate Criminal Cases': criminal_case }) 
df.to_csv('data.csv', index=False, encoding='utf-8')


print(len(candidate_edu_details))
print(len(candidate_name))
print(len(candidate_party))
print(len(candidate_age))
print(len(so_wo))
print(len(candidate_edu_details))
print(len(assets_liabilitie))
print(len(candidate_self_professions))
print(len(candidate_spouse_professions))

# result= [id.split('_')[0] for id in all_link]
# print(all_link)

   # project_href = [i['href'] for i in data.find('a', href=True)]
   # print(project_href)

# print(all_link)
# for s in all_link:
#    spt= s.split('=')
#    print(spt)



# print(link.data)

# all= link[:14]
# print(link.prettify)
# for anchor in all.find_all:
#     print(anchor.text)




































# for id in range(4871,6207):
#    url= base_url+str(id)
#    response= requests.get(url)
#    soup= BeautifulSoup(response.content, 'html.parser')
#    print('Page no- ', url)

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
