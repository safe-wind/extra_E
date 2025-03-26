<<<<<<< HEAD
# Scrivi una funzione che somma tutti i numeri interi 
# di una lista che sono maggiori di un dato valore intero 
# definito threshold.

def sum_above_threshold(numbers: list[int], threshold:int) -> int:

    somma = 0

    for number in numbers:
        if number > threshold:
            somma += number
        else:
            continue
    
    return somma



    
=======
#Create a Car class with two instance attributes:

# 1. color, which stores the name of the car’s color as a string
# 2. mileage, which stores the number of miles on the car as an integer

# Then create two Car objects—a blue car with twenty
# thousand miles and a red car with thirty thousand miles—and print out
# their colors and mileage

class Car:

    def __init__(self, color:str, mileage:float) -> None:

        self.color = color
        self.mileage = mileage
    
    def infoCar(self) -> None:
        
        print(f"The car is {self.color}, with a mileage of {self.mileage:,} miles")

maserati = Car("blue", 1999.9)
ferrari = Car("red", 3)
porsche = Car("white", 23000)

ferrari.infoCar()
porsche.infoCar()

>>>>>>> 09af9ae (es extra)
