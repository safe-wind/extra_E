# Scrivi una funzione che elimini dalla lista dati certi elementi
#  specificati in un dizionario. Il dizionario contiene elementi da
#  rimuovere come chiavi e il numero di volte che devono essere 
# rimossi come valori.
#For example:

# Test	Result
# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
# [1, 3, 4]
# print(rimuovi_elementi([], {2: 1})) 
# []

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for element in lista:
        
        for k in da_rimuovere.keys():
            
            if k in lista and da_rimuovere[k] > 0:
                if k == element:
                    lista.remove(element)
                    da_rimuovere[k] -= 1
                
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))