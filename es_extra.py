# Scrivi una funzione che calcola 
# la media di una lista di numeri e ritorna
# il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[float]) -> int:

    elements = len(numbers)
    somma = 0

    for i in numbers:

        somma += i
    
    media = somma/elements
    return round(media)
    
print(rounded_average([1, 1, 2, 2]))
