# Scrivi una funzione che riceva in input due liste di interi 
# della stessa lunghezza.
# La funzione deve calcolare la somma elemento per elemento e
# restituire una nuova lista contenente i risultati.

def somma_elementi(lst1:list[int], lst2:list[int]) -> list[int]:

    lst3 = lst1.copy()

    for i in range(0,len(lst2)):

        lst3[i] += lst2[i]
    
    return lst3

    

print(somma_elementi([1,1,1],[1,1,1]))