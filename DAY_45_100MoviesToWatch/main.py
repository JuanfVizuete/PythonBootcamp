import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

# Obtain the title html line from the movie
movies = soup.find_all(name="h3", class_="title")
#print(movies)
#Create a list with the movie titles
movie_titles = [title.getText() for title in movies]
movie_titles.reverse()
print(movie_titles)

with open('movies.txt', mode='w', encoding='utf-8') as file:
    for title in movie_titles:
        file.write(title + "\n")

