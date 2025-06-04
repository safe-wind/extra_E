
# Scrivi una funzione che prenda una lista di numeri 
# e ritorni un dizionario che classifichi i numeri in liste separate 
# per numeri positivi e negativi.

def order_pos_neg(lista_1:list[float]) -> dict[float]:

    dict_1:dict = dict()
    lista_positivi:list= list()
    lista_negativi:list= list()

    for element in lista_1:

        if element < 0:
            lista_negativi.append(element)
        else:
            lista_positivi.append(element)
        
    dict_1["positivi"] = lista_positivi
    dict_1["negativi"] = lista_negativi

    return dict_1

list1 = [-1,-2,-3,-4,-5,1,2,3,4]

dict2 = order_pos_neg(list1)

print(dict2)