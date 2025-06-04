
def prodotto(lista_interi:list[int], valore_threshold:int) -> int:

    risultato = 1

    for element in lista_interi:

        if element < valore_threshold:

            risultato*=element
        
    return risultato


lista = [3, 7, 2, 9, 5]
threshold = 6

print(prodotto(lista, threshold))
