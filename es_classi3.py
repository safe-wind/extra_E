# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, 
# ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona():

    def __init__(self, nome:str, eta:int, sesso:str) -> None:
        self.name = nome
        self.age = eta
        self.gender = sesso
    
    def presentati(self) -> None:
        return print(f"Ciao, mi chiamo {self.name} e ho {self.age} anni")

persona1 = Persona("Mario", 32, "maschio")

persona1.presentati()
