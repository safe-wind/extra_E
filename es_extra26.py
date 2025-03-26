<<<<<<< HEAD
#Scrivi una funzione che ritorna il valore massimo, 
# minimo e la media di una lista di numeri interi.

def list_statistics(lst: list[int]) -> tuple:

    elements = len(lst)
    somma = 0

    num_max = max(lst)
    num_min = min(lst)

    for x in lst:

        somma+=x
    
    media = somma/elements

    return num_max, num_min, media

print(list_statistics([1, 2, 3, 4, 5]))
=======
# Create a GoldenRetriever class that inherits from the Dog class.
# Give the sound argument of GoldenRetriever.speak() a default value of "Bark".

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:                           # __str__(self)
        return f"{self.name} is {self.age} years old"   # permette di "decriptare" l'oggetto 
                                                        # localizzato all'indirizzo main in memoria

    def speak(self, sound) -> str:
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):

    def speak(self, sound="Bark!") -> None:
        print(f"{self.name} says {sound} {sound}")

marley = GoldenRetriever("Marley", 2)
scruffle = Dog("Scruffle", 4)

print(type(marley.speak()))
print(scruffle.speak("ouuuu"))
print(scruffle)
>>>>>>> 09af9ae (es extra)
