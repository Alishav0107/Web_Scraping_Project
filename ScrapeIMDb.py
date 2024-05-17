
from bs4 import BeautifulSoup
import requests  , openpyxl

def generateExcelFile():
    excel = openpyxl.Workbook()
    # print(excel.sheetnames)
    sheet = excel.active
    sheet.title = 'Top Rated Movies'
    # print(excel.sheetnames)
    sheet.append(['Movie Rank', 'Movie Name' ,'Year Of Release','IMDB Rating'])


    try:
        source = requests.get('https://www.imdb.com/chart/top/')
        source.raise_for_status()

        soup = BeautifulSoup(source.text , "html.parser") 

        movies = soup.find('tbody', class_="lister-list").find_all('tr')
        # print(len(movies))
        for movie in movies:

            name = movie.find('td' , class_="titleColumn").a.text

            rank = movie.find('td', class_="titleColumn").get_text (strip = True).split('.')[0]
            # print(name)
            # print(rank)
            year = movie.find('td', class_="titleColumn").span.text.strip('()')
            # print(year)
            rating = movie.find('td' , class_="ratingColumn imdbRating").strong.text
            # print(rating)

            # print( rank,name ,  year, rating)
            sheet.append([rank ,name, year, rating])

            # break

    except Exception as err:
        print(err)

    excel.save('files/IMDB_Movie_Rating.xlsx')