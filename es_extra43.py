# Dopo aver ricevuto una stringa, la funzione deve contare quante vocali contiene.
# Per “casa”, il risultato è 2.
# Questo esercizio aiuta a lavorare sulla scansione carattere per carattere con la ricorsione, 
# permettendo di comprendere come filtrare elementi di una sequenza.

def contaVocali(text:str) -> int:
    # Caso base: stringa vuota
    if len(text) == 0:
        return 0
    
    prima_lettera = text[0]
    cont = 0

    if prima_lettera in 'aeiou':
        cont = 1

    return cont + contaVocali(text[1:])
    

print(contaVocali("casa"))

