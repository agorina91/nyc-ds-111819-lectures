# Each of the following functions can be defined in the `functions.py` file. 

# * **Searching functions**
#   * Find by name - Takes in a string that represents the name of an album. Should return a dictionary with the correct album, or return `None`.
#   * Find by rank - Takes in a number that represents the rank in the list of top albums and returns the album with that rank. If there is no album with that rank, it returns `None`.
#   * Find by year - Takes in a number for the year in which an album was released and returns a list of albums that were released in that year. If there are no albums released in the given year, it returns an empty list.
#   * Find by years - Takes in a start year and end year. Returns a list of all albums that were released on or between the start and end years. If no albums are found for those years, then an empty list is returned. 
#   * Find by ranks - Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks. If no albums are found for those ranks, then an empty list is returned.
# * **All functions**
#   * All titles - Returns a list of titles for each album.
#   * All artists - Returns a list of artist names for each album.
# * **Questions to answer / functions**
#   * Artists with the most albums - Returns the artist with the highest amount of albums on the list of top albums 
#   * Most popular word - Returns the word used most in amongst all album titles
#   * Histogram of albums by decade - Returns a histogram with each decade pointing to the number of albums released during that decade.
#   * Histogram by genre - Returns a histogram with each genre pointing to the number of albums that are categorized as being in that genre.

import csv
import csv
with open('/Users/agorina/Desktop/Flatiron/nyc-ds-111819-lectures/Mod_1/rolling-stones/data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    alist = [i for i in reader]


#   * Find by name - Takes in a string that represents the name of an album. 
# Should return a dictionary with the correct album, or return `None`.
def find_by_name(album_name):
    for dic in alist:
        
        if album_name == dic['album']:
            return dic

    return None
        
#   * Find by rank - Takes in a number that represents the rank in the list of top albums 
#and returns the album with that rank. If there is no album with that rank, it returns `None`.        
def find_by_rank(number):
    for dic in alist:
        if number == dic['number']:
            return dic
        
    return None
        

#   * Find by year - Takes in a number for the year in which an album was released 
#and returns a list of albums that were released in that year. 
#If there are no albums released in the given year, it returns an empty list.


def find_by_year(year):
    year_list = []
    for dic in alist:
        if year == dic['year']:
            year_list.append(dic)
    return year_list
    return None


#   * Find by years - Takes in a start year and end year. 
#Returns a list of all albums that were released on or between the start and end years. 
#If no albums are found for those years, then an empty list is returned. 

def find_by_years(start_year, end_year):
    years_list = []
    for dic in alist:
        if int(dic['year']) in range(int(start_year), int(end_year)):
            years_list.append(dic)
            
    return years_list
            
            
            
#   * Find by ranks - Takes in a start rank and end rank. 
#Returns a list of albums that are ranked between the start and end ranks. 
#If no albums are found for those ranks, then an empty list is returned.



def find_by_ranks(start_rank, end_rank):
    list_of_ranks = []
    for dic in alist:
        if int(dic['number']) in range(int(start_rank), int(end_rank)+1): #increased by one assuming we want to include endrank
            list_of_ranks.append(dic)
            
    return list_of_ranks


#   * All titles - Returns a list of titles for each album.

def all_titles():
    list_of_titles = []
    for dic in alist:
        titles = dic['album']
        list_of_titles.append(titles)
        
    return list_of_titles

#   * All artists - Returns a list of artist names for each album.

def all_artists():
    list_of_artists = []
    for dic in alist:
        artist = dic['artist']
        list_of_artists.append(artist)
        
    return list_of_artists


list_of_artists = []
for dic in alist:
    artist = dic['artist']
    list_of_artists.append(artist)
    
list_of_artists

#   * Artists with the most albums - 
# Returns the artist with the highest amount of albums on the list of top albums 

from collections import Counter
data = Counter(list_of_artists)
data.most_common()   
data.most_common(1) 


#   * Most popular word - 
# Returns the word used most in amongst all album titles

just_words = []
for word in list_of_titles:
    just_words.append(word)
    


data = Counter(just_words)
data.most_common()   
data.most_common(1) 
        