class Movie:
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return (f"""Title: {self.title}"
                Year: {self.year}"
                Director: {self.director}"
                Rating: {self.rating}"
                Genre: {self.genre}"
                Cast: {self.cast}")
"""
# Sample movie instances
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
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", "Robert De Niro, Ray Liotta, Joe Pesci"),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", "Jodie Foster, Anthony Hopkins, Scott Glenn"),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", "Leonardo DiCaprio, Kate Winslet, Billy Zane"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", "Elijah Wood, Ian McKellen, Orlando Bloom"),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", "Russell Crowe, Joaquin Phoenix, Connie Nielsen"),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", "Tom Hanks, Michael Clarke Duncan, David Morse"),
    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", "Tom Hanks, Matt Damon, Tom Sizemore"),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", "Sam Neill, Laura Dern, Jeff Goldblum"),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", "Leonardo DiCaprio, Matt Damon, Jack Nicholson"),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", "Matthew Broderick, Jeremy Irons, James Earl Jones"),
    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", "Jim Carrey, Kate Winslet, Kirsten Dunst")
]

# Functions for sorting and searching
def sort_movies_alphabetically(movie_list):
    return sorted(movie_list, key=lambda x: x.title)

def sort_movies_chronologically(movie_list):
    return sorted(movie_list, key=lambda x: x.year)

def search_by_genre(movie_list, genre):
    return [movie for movie in movie_list if movie.genre.lower() == genre.lower()]

def search_by_director(movie_list, director):
    return [movie for movie in movie_list if movie.director.lower() == director.lower()]

def search_by_cast(movie_list, cast_member):
    return [movie for movie in movie_list if cast_member.lower() in movie.cast.lower()]

# Examples of using the methods
print("All movies sorted alphabetically:")
for movie in sort_movies_alphabetically(movies):
    print(movie)

print("\nAll movies sorted chronologically:")
for movie in sort_movies_chronologically(movies):
    print(movie)

# Example search functions
print("\nSearch results for genre 'Drama':")
for movie in search_by_genre(movies, "Drama"):
    print(movie)

print("\nSearch results for director 'Steven Spielberg':")
for movie in search_by_director(movies, "Steven Spielberg"):
    print(movie)

print("\nSearch results for cast member 'Leonardo DiCaprio':")
for movie in search_by_cast(movies, "Leonardo DiCaprio"):
    print(movie)
