# Bisogna scrivere una funzione ricorsiva che stampi il primo carattere di una stringa. 
# Se l’input è “Python”, il programma deve stampare “P”.
# Questo esercizio è molto semplice, ma serve per far prendere confidenza con la gestione delle stringhe
# e il concetto di caso base.

def charFirst(text:str, lenght:int) -> str:

    if lenght < 1:
        return 0
    
    elif lenght == 1:
        return text[0]
    
    else:
        return charFirst(text, lenght-1)
    

print(charFirst("Python", 6))