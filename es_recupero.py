# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
# la chiave è già presente, somma il valore al valore già associato alla chiave.

def convert_list_of_tuple(list_1:list[tuple]) -> dict:

    dict_1:dict = dict()

    for element in list_1:

        key, value = element[0], element[1]

        if key in dict_1:
            dict_1[key] += value

        if key not in dict_1:
            dict_1[key] = value
    
    return dict_1

lista1:list[tuple] = [("uno",1),("due",2),("tre",3),("due",2)]

dict2: dict = convert_list_of_tuple(lista1)

print(dict2)