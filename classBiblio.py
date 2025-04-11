
class Libro:

    def __init__(self):
        self.titolo = ""
        self.autore = ""
        self.genere = []

    def set_titolo(self, titolo:str) -> None:
        self.titolo = titolo
    
    def set_autore(self, autore:str) -> None:
        self.autore = autore
    
    def set_genere(self, lista_genere:list[str]) ->None:
        self.genere = lista_genere
    
    def get_autore(self) -> str:
        return self.autore
    def get_titolo(self) -> str:
        return self.titolo
    def get_genere(self) -> list[str]:
        return self.genere
    
class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []

    def set_libro(self, libro:Libro) -> None:
        self.libri.append(libro)
    
    def get_libri_titolo(self) -> str:
        for item in self.libri:
            print(item.get_titolo())


collezione:Biblioteca = Biblioteca()

piccolo_principe:Libro = Libro()
piccolo_principe.set_autore("Sconosciuto")
piccolo_principe.set_genere(["Narrativa"])
piccolo_principe.set_titolo("Piccolo Principe")

fn:Libro = Libro()
fn.set_titolo("Le avventure di Federico March")
fn.set_autore("Federico March")
fn.set_genere(["Drama", "Comico"])

print(fn.get_autore(), fn.get_genere(), fn.get_titolo())
print(piccolo_principe.get_autore(), piccolo_principe.get_genere(), piccolo_principe.get_titolo())

collezione.set_libro(piccolo_principe)
collezione.set_libro(fn)

collezione.get_libri_titolo()