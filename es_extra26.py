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