from bs4 import BeautifulSoup
import requests,openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Top Rated Movies"#changing sheet name

sheet.append(['Movie Rank','Ttile',"Year of Release",'imbd Rating'])#append column
try:
    source=requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()#this will raise error if url is not correct
    soup=BeautifulSoup(source.text,"html.parser")
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        name=movie.find("td",class_="titleColumn").a.text
        rank=movie.find("td",class_="titleColumn").get_text(strip=True).split('.')
        year=movie.find("td",class_="titleColumn").span.text.strip("()")
        rating=movie.find("td",class_="ratingColumn imdbRating").strong.text

        print(rank[0],name,year,rating)
        sheet.append([rank[0],name,year,rating])

except Exception as e:
     print(e)
excel.save('Imbd Movie Rating.xlsx')
