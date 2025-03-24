# Creare due tuple che rappresentino i due
# elenchi di nomi e cognomi descritti sotto:
# nomi: Numa, Tullo, Anco
# cognomi: Pompilio, Ostilio, Marzio
# ● Ottenere una lista in cui ogni elemento è un
# dizionario {'nome': nome, 'cognome':
# cognome}, che accoppia nomi e cognomi in
# base all'ordine.

nomi:tuple = ("Numa", "Tullo", "Anco")
cognomi:tuple = ("Pompilio", "Ostilio", "Marzio")

lst_nc:list[str,str] = list()

i=0
while i < 3:
    nome = nomi[i]
    cognome = cognomi[i]
    dzn: dict[str,str] = {"Nome":nome,
                            "Cognome": cognome}
    lst_nc.append(dzn)
    i+=1
    

print(lst_nc)
    
    