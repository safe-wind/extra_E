

# 3) Scrivi una funzione che accetti un dizionario di prodotti 
# con i relativi prezzi e restituisca un nuovo dizionario con 
# solo i prodotti che hanno un prezzo inferiore a 50, ma con i 
# prezzi aumentati del 10% e arrotondati a due cifre decimali.

def prodotti_min50_incr10(dict1:dict[str,float]) -> dict:
    
    dict_agg:dict = dict()

    for key, value in dict1.items():

        if dict1[key] < 50:
            
            new_value = round(value*1.10, 2)
            dict_agg[key] = new_value
    
    return dict_agg


prodotti = {
    "penna": 1.50,
    "zaino": 55.00,
    "quaderno": 3.20,
    "calcolatrice": 45.90,
    "libro": 60.00
}

print(prodotti_min50_incr10(prodotti))

