# Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

class Animale:

    def __init__(self, nome:str, specie:str) -> None:
        self.nome=nome.lower()
        self.specie=specie.lower()

    def emetti_suono(self) -> None:

        if self.specie == "q":
            print("Quantastic!")

        if self.specie == "gatto":
            return print("Miao!")
        
        elif self.specie == "cane":
            return print("Bau!")
        
        else:
            return print("I have no animal like this ")


animal1 = Animale("Pringles", "gatto")

animal1.emetti_suono()