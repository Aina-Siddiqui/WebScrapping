import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
url="https://www.basketball-reference.com/players/"
header=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
         'Accept-language':'en-US,en;q=0.5'})
webpage=requests.get(url,headers=header)
soup=BeautifulSoup(webpage.content,'html.parser')
players=soup.find_all('td')

playersul=[]
links=[]
names=[]
no_of_games=[]
pts=[]
trb=[]
ast=[]

for p in players:
       playersul.append(p.find('a'))

for playerul in playersul:
     links.append("https://www.basketball-reference.com/"+playerul.get('href'))

for link in links:
     r=requests.get(link)
     soup2=BeautifulSoup(r.content,'html.parser')

     name=soup2.find('h1').text.strip()
     names.append(name)
     info=soup2.find('div',class_="p1")
     allpara=info.find_all('p')

     no_of_games.append(allpara[1].text)
     pts.append(allpara[3].text)
     trb.append(allpara[5].text)
     ast.append(allpara[7].text)






df=pd.DataFrame({
    "Name":names,
    "Games":no_of_games,
    "Points":pts,
    "Total Rebound":trb,
    "Assists":ast,

})
df.to_csv("basketball players.csv",header=True,index=False)
#
#
# #
# #
# #
# #
