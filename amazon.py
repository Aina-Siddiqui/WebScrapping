from bs4 import BeautifulSoup
import requests,openpyxl
import pandas as pd


url="https://www.amazon.com/s?k=ps5&ref=nb_sb_noss"
header=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
         'Accept-language':'en-US,en;q=0.5'})
webpage=requests.get(url,headers=header)
soup=BeautifulSoup(webpage.content,'html.parser')
links=soup.find_all('a',class_="a-link-normal s-no-outline")
new_webpages=[]

for link in links:
    new_link="https://amazon.com"+link.get("href")
    new_webpages.append(new_link)
headings=[]
prices=[]
for new in new_webpages:
    r=requests.get(new,headers=header)
    soup2=BeautifulSoup(r.content,"html.parser")
    heading=soup2.find("span",id="productTitle").text
    headings.append("PS5"+heading)
    price=soup2.find('span',class_="a-price-whole").text
    prices.append(price)



amazon=pd.DataFrame({
     'title':headings,
      "link":new_webpages,
      "price":prices

 })
amazon.to_csv("amazon.csv",header=True,index=False)


