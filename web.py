port openpy
import request
from bs4 import beautifulsoup

excel=openpy.workbook()
sheet=excel.active
sheet.title="movie list"
sheet.append(['rank','movie_name','year of release','IMBD rating'])


try:
     response=request("https://www.imdb.com/chart/top/")
     soup=beautifulsoup(response.text,'html.parser')
     movie=soup.find('tbody',class_="lister_list")find_all("tr")

     for movie in movies:
         rank=movie.find('td',class_="title column").gettext(srip=true).split('.')[0]
         movie_name=movie.find('td',class_="title column").a.text
         rate=movie.find('td',class_="rating column").strong.text
         year=movie.find('td',class_="title column").span.text.replace('(',"))
         year=year.replace(')',"")
         sheet.append([rank,movie_name,year,rate])

 except Exception as e:
         print(e)
         excel.save("movies.xlsx")
im
