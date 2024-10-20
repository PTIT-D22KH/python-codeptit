# pykt076.py
from datetime import datetime
class Genre:
    count = 0
    genre_dict = {}
    def __init__(self, name):
        Genre.count += 1
        self.id = f"TL{Genre.count:03d}"
        self.name  = name
        Genre.genre_dict[self.id] = name
    def __str__(self):
        return self.name

class Film:
    count = 0
    def __init__(self, genreId, startDate, name, numEpisodes):
        self.genreId = genreId
        self.startDateString = startDate
        # datetime.strftime
        self.startDate = datetime.strptime(startDate, "%d/%m/%Y")
        self.name = name
        self.numEpisodes = int(numEpisodes)
        Film.count += 1
        self.filmId = f"P{Film.count:03d}"

    def __str__(self):
        return self.filmId + " " + Genre.genre_dict[self.genreId] + " " + self.startDateString + " " + self.name + " " + str(self.numEpisodes)
        

def cmp(a):
    return (a.startDate, a.name, -a.numEpisodes)
        
def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    genres = []
    films = []
    for i in range(n):
        genres.append(Genre(input()))
    for i in range(m):
        films.append(Film(input(), input(), input(), input()))
    films.sort(key = cmp)
    for x in films:
        print(str(x))

if __name__ == '__main__':
    main()
