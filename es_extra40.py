# L’esercizio chiede di scrivere una funzione ricorsiva per contare quanti numeri pari ci sono in un array. 
# Ad esempio, dato [1, 4, 6, 3, 2], il risultato sarà 3.
# Qui si introduce l’idea di esplorare un array elemento per elemento, 
# accumulando il conteggio in una struttura ricorsiva.

def countPari(arr:list[int], dim:int) -> int:

    if dim <= 0:
        return 0
    
    elif arr[dim-1]%2==0:
        return 1+ countPari(arr, dim-1) #se l'ultimo num della lista è pari setto la ricorsione partendo da 1
    else:
        return 0+ countPari(arr, dim-1) #sel l'ultimo num della lista è dispari setto la ricorsione partendo da 0




print(countPari([1, 4, 2, 2, 2], 5))