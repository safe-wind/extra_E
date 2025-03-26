# Scrivi una funzione che unisce due dizionari. 
# Se una chiave è presente in entrambi, somma i loro valori.


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
    new_dict = dict1.copy()
    
    for k1, v1 in dict2.items():

        if k1 in dict1.keys():
            new_dict[k1] += v1 
            
    return new_dict

print(merge_dictionaries({'x': 0}, {'x': -5}))
