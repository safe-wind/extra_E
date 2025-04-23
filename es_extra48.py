# Scrivi una funzione che prenda in input una lista di dizionari che
#  rappresentano voti di studenti e aggrega i voti per studente in un 
# nuovo dizionario.

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:

    dizionario_voti = {}

    for element in voti:
        nome = element['nome']
        voto = element['voto']
        
        if nome in dizionario_voti:
            dizionario_voti[nome].append(voto)
        else:
            dizionario_voti[nome] = [voto]
    
    return dizionario_voti

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))