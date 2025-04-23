#Scrivi una funzione che inverte le chiavi e i valori in un dizionario.
# Se ci sono valori duplicati, scarta i duplicati.
# For example:

# Test	Result
# print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
# {1: 'a', 2: 'b', 3: 'c'}
# print(inverti_mappa({}))
# {}

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    nuovo_dizionario = {}

    for k, v in dizionario.items():
        
        if v not in nuovo_dizionario:
            nuovo_dizionario[v] = k

    return nuovo_dizionario

print(inverti_mappa({'a': 1, 'b': 2, 'c': 4}))