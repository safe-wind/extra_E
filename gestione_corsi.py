# In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
# Il sistema gestisce aule ed edifici (Parte 1), 
# persone -studenti e docenti- in gruppi di studio (parte 2),
# e corsi (parte 3).
 
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), 
# un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), 
# un intervallo di piani (floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo
#       di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

class Room:
    def __init__(self, id, floor, seats):
        self._id = id
        self._floor = floor
        self._seats = seats
        self._area = seats * 2  # L'area è il doppio dei posti

    def get_id(self):
        return self._id

    def get_floor(self):
        return self._floor

    def get_seats(self):
        return self._seats

    def get_area(self):
        return self._area


class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors  # Intervallo di piani, ad esempio (0, 5)
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        # Verifica se il piano dell'aula è compreso nell'intervallo dei piani dell'edificio
        min_floor, max_floor = self.floors
        if min_floor <= room.get_floors() <= max_floor:
            self.rooms.append(room)
        else:
            print(f"Errore: Aula {room.get_id()} su piano {room.get_floor()} non valida per l'edificio '{self.name}'.")

    def area(self):
        # Somma delle aree di tutte le aule
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area
