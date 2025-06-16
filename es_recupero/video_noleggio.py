

class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = None):
        self._customer_id = customer_id
        self._name = name
        self._rented_movies = rented_movies if rented_movies is not None else []

    def rent_movie(self, movie: Movie): 
        if not movie._is_rented:
            movie.rent()
            self._rented_movies.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato")

    def return_movie(self, movie: Movie): 
        if movie in self._rented_movies:
            movie.return_movie()
            self._rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")

    def __str__(self):
        if self._rented_movies:
            elenco: str = ", ".join(i._title for i in self._rented_movies)
        else:
            elenco = "Nessun film noleggiato"
        return f"ID: {self._customer_id}, Nome: {self._name}, Rented Movies: {elenco}"


class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False) -> None:
        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._is_rented = is_rented

    def rent(self) -> None:
        if not self._is_rented:
            self._is_rented = True
        else:
            print(f"Il film {self.title} è già noleggiato")

    def return_movie(self) -> None:
        if self._is_rented:
            self._is_rented = False
        else:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente")

    def __str__(self):
        stato = "no" if self._is_rented else "si"
        return f"Id: {self._movie_id}, Titolo: {self._title}, Director: {self._director}, Disponibile: {stato}"

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = None, customers: dict[str, Customer] = None) -> None:
        self._movies =  movies if movies is not None else {}
        self._customers = customers if customers is not None else {}

    def add_movie(self, movie_id: str, title: str, director: str) -> None: 
        if movie_id not in self._movies:
            m: Movie = Movie(movie_id, title, director)
            self._movies[movie_id] = m
        else:
            print(f"Il film con ID {movie_id} esiste già")

    def register_customer(self, customer_id: str, name: str) -> None: 
        if customer_id not in self._customers:
            c:Customer = Customer(customer_id, name)
            self._customers[customer_id] = c
        else:
            print(f"Il cliente con ID {customer_id} è già registrato")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self._customers and movie_id in self._movies:
            self._customers[customer_id].rent_movie(self._movies[movie_id])
        else:
            print("Cliente o film non trovato")

    def return_movie(self, customer_id: str, movie_id: str) -> None: 
        if customer_id in self._customers and movie_id in self._movies:
            self._customers[customer_id].return_movie(self._movies[movie_id])
        else:
            print("Cliente o film non trovato")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self._customers:
            return self._customers[customer_id]._rented_movies
        else: 
            print("Cliente non trovato")
            return []
        
    def __str__(self) -> str:
        if self._movies:
            elenco1:str = " \n".join(str(i) for i in self._movies.values())
        else:
            elenco1 = "Nessun film registrato"
       
        if self._customers:
            elenco2:str =  " \n".join(str(i) for i in self._customers.values())
        else:
            elenco2 = "Nessun utente registrato"
        
        return f"\nFilm\n{elenco1} \nUtenti\n{elenco2}"
