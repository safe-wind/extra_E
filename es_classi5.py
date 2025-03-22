# Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. 
# Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio 
# “Questa è una Toyota Corolla del 2017”.

class Automobile:

    def __init__(self, marca:str, modello:str, anno:int) -> None:
        self.marca = marca
        self.modello:str = modello
        self.anno = anno
    
    def descrivi(self) -> None:
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")

auto1 = Automobile("Alfa R.", "Stelvio", 2024)

auto1.descrivi()

