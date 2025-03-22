# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% 
# e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio
# “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:

    def __init__(self, nome:str, cognome:str, matricola:int, stipendio:int) -> None:

        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio 

    def aumentaStipendio(self)-> int:
        self.stipendio += self.stipendio*0.1

    
    def stampaDettagli(self) -> None:
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio: {self.stipendio:.2f} Euro")

impiegato1 = Impiegato("Marco", "Rossi", 123456, 3000)

impiegato1.stampaDettagli() 

impiegato1.aumentaStipendio()
impiegato1.aumentaStipendio()
impiegato1.aumentaStipendio()

impiegato1.stampaDettagli()