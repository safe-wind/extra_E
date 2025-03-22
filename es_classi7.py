# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
# La classe dovrà avere i seguenti metodi:
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.


class Prodotto:
    
    def __init__(self, nome:str, prezzo:float, scorta:float) ->None:
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta
    
    def costMgzn(self, costo_mgzn:float = 0.1) -> None:
        costo_mgzn = self.scorta * costo_mgzn

        return costo_mgzn

class GestoreMagazzino:


    def __init__(self, costo_mgzn:float = 0.1):

        prodotti:dict[str,float] = dict()
        self.prodotti = prodotti

        self.costo_mgzn = costo_mgzn
    
    def aggiungiProdotto(self, prodotto:str) -> None:
        
        self.prodotti[prodotto.nome] = prodotto
    
    def rimuoviProdotto(self, prodotto:str) -> None:

        self.prodotti.pop(prodotto)


    def costMgzn(self, costo_mgzn:float = 0.1) -> float:

        costo_mgzn = self.scorta * costo_mgzn

        return costo_mgzn
    
    def show(self) -> None:

        for k, v in (self.prodotti).items():

            print(f"{k}: {v}")

    
    

prodotto1 = Prodotto("fragola", 5, 5)
prodotto2 = Prodotto("kiwi", 7, 15)
prodotto3 = Prodotto("limone", 10, 40)
gm = GestoreMagazzino()

gm.aggiungiProdotto(prodotto2)
gm.aggiungiProdotto(prodotto1)
gm.show()
print(f"Costo stoccaggio p/g: {prodotto1.costMgzn()}€")
print(f"Nome Prodotto : {prodotto1.nome}")
print(f"Quantità: {prodotto1.scorta}kg")





    




        
