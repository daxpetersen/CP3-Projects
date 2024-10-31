class Movie:
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"""Title: {self.title}
Year: {self.year}
Director: {self.director}
Rating: {self.rating}
Genre: {self.genre}
Cast: {self.cast}"""


class MovieCollection:
    def __init__(self, movies):
        self.movies = movies

    def sort_alphabetically(self):
        self.movies.sort(key=self.get_title)
        return "\n\n".join(str(movie) for movie in self.movies)

    def sort_chronologically(self):
        self.movies.sort(key=self.get_year)
        return "\n\n".join(str(movie) for movie in self.movies)

    def get_title(self, movie):
        return movie.title

    def get_year(self, movie):
        return movie.year

    def search_by_genre(self, genre):
        matching_movies = []
        for movie in self.movies:
            if movie.genre.lower() == genre.lower():
                matching_movies.append(str(movie))
        return "\n\n".join(matching_movies)

    def search_by_director(self, director):
        matching_movies = []
        for movie in self.movies:
            if movie.director.lower() == director.lower():
                matching_movies.append(str(movie))
        return "\n\n".join(matching_movies)

    def search_by_cast(self, cast_member):
        matching_movies = []
        for movie in self.movies:
            if cast_member.lower() in movie.cast.lower():
                matching_movies.append(str(movie))
        return "\n\n".join(matching_movies)


movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", "Tim Robbins, Morgan Freeman"),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", "Marlon Brando, Al Pacino, James Caan"),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", "John Travolta, Uma Thurman, Samuel L. Jackson"),
    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page"),
    Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss"),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", "Tom Hanks, Robin Wright, Gary Sinise"),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", "Christian Bale, Heath Ledger, Aaron Eckhart"),
    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", "Liam Neeson, Ben Kingsley, Ralph Fiennes"),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", "Brad Pitt, Edward Norton, Helena Bonham Carter"),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", "Robert De Niro, Ray Liotta, Joe Pesci")
]

collection = MovieCollection(movies)
print("Movies sorted alphabetically:")
print(collection.sort_alphabetically())

print("\nMovies sorted chronologically:")
print(collection.sort_chronologically())

print("\nSearch results for genre 'Drama':")
print(collection.search_by_genre("Drama"))

print("\nSearch results for director 'Steven Spielberg':")
print(collection.search_by_director("Steven Spielberg"))

print("\nSearch results for cast member 'Leonardo DiCaprio':")
print(collection.search_by_cast("Leonardo DiCaprio"))