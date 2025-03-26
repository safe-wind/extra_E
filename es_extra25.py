
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
