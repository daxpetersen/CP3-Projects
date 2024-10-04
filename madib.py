
"""




















Inglourious Basterds, (2009), Quentin Tarantino, R, War, [Brad Pitt, Christoph Waltz, Mélanie Laurent]

The Sixth Sense, (1999), M. Night Shyamalan, PG-13, Thriller, [Bruce Willis, Haley Joel Osment, Toni Collette]

The Usual Suspects, (1995), Bryan Singer, R, Mystery, [Kevin Spacey, Gabriel Byrne, Chazz Palminteri]

Memento, (2000), Christopher Nolan, R, Thriller, [Guy Pearce, Carrie-Anne Moss, Joe Pantoliano]

Braveheart, (1995), Mel Gibson, R, Biography, [Mel Gibson, Sophie Marceau, Patrick McGoohan]

The Terminator, (1984), James Cameron, R, Sci-Fi, [Arnold Schwarzenegger, Linda Hamilton, Michael Biehn]

Back to the Future, (1985), Robert Zemeckis, PG, Adventure, [Michael J. Fox, Christopher Lloyd, Lea Thompson]

Alien, (1979), Ridley Scott, R, Horror, [Sigourney Weaver, Tom Skerritt, John Hurt]

The Truman Show, (1998), Peter Weir, PG, Drama, [Jim Carrey, Laura Linney, Noah Emmerich]
"""
list = []
class movie():
    def __init__(self, title, year, director, rating, genre, staff):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.staff = staff

    def __str__(self):
        return f"""
        Name: {self.title}
        Year: {self.year}
        Director: {self.director}
        Rating: {self.rating}
        Genre: {self.genre}
        Staff: {self.staff}
        """
            
Redemption = movie("The Shawshank Redemption",1994, "Frank Darabont", "R", "Drama", "Tim Robbins, Morgan Freeman")
list.append(1994)

Godfather = movie("The Godfather",1972, "Francis Ford Coppola", "R", "Crime", "Marlon Brando, Al Pacino, James Caan")
list.append(1972)

Pulp = movie("Pulp Fiction",1994, "Quentin Tarantino", "R", "Crime", "John Travolta, Uma Thurman, Samuel L. Jackson")
list.append(1994)

Inception = movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page")
list.append(2010)

Matrix = movie("The Matrix",1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")
list.append(1999)

Gump = movie("Forrest Gump",1994, "Robert Zemeckis", "PG-13", "Drama", "Tom Hanks, Robin Wright, Gary Sinise")
list.append(1994)

Knight = movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", "Christian Bale, Heath Ledger, Aaron Eckhart")
list.append(2008)

Schindler = movie("Schindler List", 1993, "Steven Spielberg", "R", "Drama", "Liam Neeson, Ben Kingsley, Ralph Fiennes")
list.append(1993)

Club = movie("Fight Club", 1999, "David Fincher", "R", "Drama", "Brad Pitt, Edward Norton, Helena Bonham Carter")
list.append(1999)

Goodfellas = movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", "Robert De Niro, Ray Liotta, Joe Pesci")
list.append(1990)

Lambs = movie("The Silence of The Lambs", 1991, "Jonathan Demme", "R", "Thriller", "Jodie Foster, Anthony Hopkins, Scott Glenn")
list.append(1991)

Titanic = movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", "Leonardo DiCaprio, Kate Winslet, Billy Zane")
list.append(1997)

Rings = movie("The Lord of The Rings, The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", "Elijah Wood, Ian McKellen, Orlando Bloom")
list.append(2001)

Gladiator = movie("Gladiator", 2000, "Ridley Scott", "R", "Action", "Russell Crowe, Joaquin Phoenix, Connie Nielsen")
list.append(2000)

Mile =movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", "Tom Hanks, Michael Clarke Duncan, David Morse")
list.append(1999)

Ryan = movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", "Tom Hanks, Matt Damon, Tom Sizemore")
list.append(1998)

Park = movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", "Sam Neill, Laura Dern, Jeff Goldblum")
list.append(1993)

Departed = ("The Departed",2006, "Martin Scorsese", "R", "Crime", "Leonardo DiCaprio, Matt Damon, Jack Nicholson")
list.append(2006)

King = movie("The Lion King",1994, "Roger Allers, Rob Minkoff", "G", "Animation", "Matthew Broderick, Jeremy Irons, James Earl Jones")
list.append(1994)

Mind = movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", "Jim Carrey, Kate Winslet, Kirsten Dunst")
list.append(2004)

                
            



print(Mind)



        

