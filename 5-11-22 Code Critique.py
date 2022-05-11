#this code runs after being debugged and installing bs4...


import random #this randomly picks the movies from IMDb
import requests #this helps add parameters to finding data (ex. only listing director, movie title, year, actors, etc.)
from bs4 import BeautifulSoup #this specifically targets HTMP and XML files (compared to csv, xcell, word, etc.)

# crawl IMDB Top 250 and randomly select a movie

URL = 'http://www.imdb.com/chart/top' #this is the website in question

def main():
    response = requests.get(URL) #this tells us that we are pulling data from former link

    soup = BeautifulSoup(response.text, 'html.parser') #good for "web scraping" so I guess this means it helps comb through data
    #soup = BeautifulSoup(response.text, 'lxml') # faster #yeah I don't know what this one means lol

    # print(soup.prettify())

    movietags = soup.select('td.titleColumn') #I think these lines (20-22) just tell the computer to sort through the first comlumn (called Rank & Title on IMDb)
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag): #these lines get the year and chop it off and replace it (see split function)
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title' #ok this pulls the director's name and the big actors
    titles = [tag.text for tag in inner_movietags] #this pulls the movie name from the first column
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value' #ok this shows the rating of said movie

    n_movies = len(titles) #n_movies corresponds to a total entry containing movie title, year, rating, director, and actors

    while(True):
        idx = random.randrange(0, n_movies) #this loops continuously picks random movies on the IMDb list
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}') #this prints the data in a certain order after fetching it

        user_input = input('Do you want another movie (y/[n])? ') #This allows for users to control how long the loop goes on
        if user_input != 'y': #this means that "yes" is good for conjuring up another random movie and its data
            break
    

if __name__ == '__main__': #according to the internet, this means that data is being directly pulled and not imported from something? Ok...
    main()
