# Creare una classe Animale che abbia gli attributi 
# “nome” e “specie”. Aggiungi un metodo “emetti_suono”
#  che stampi un suono specifico per ogni specie. Ad esempio,
#  se l’animale è un gatto dovrebbe stampare “Miao!”, 
# se è un cane “Bau!”.


class Animale:

    def __init__(self, nome:str, specie:str) -> None:

        self.nome = nome
        self.specie = specie

    def suono(self):

        if self.specie == "cat":
            print("MIAOOOOO")
        elif self.specie == "dog":
            print("CIAOOOOO")


animale = Animale("C", "dog")

animale.suono()