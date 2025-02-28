#funzioni
#Scrivi una funzione che prende una stringa
#e restituisce la stringa invertita.


string_inp: str = input("Inserisci una stringa: ")

def invertita(par1: str):

    invert = par1[::-1]

    return invert


string_inv = invertita(string_inp)


print(string_inv)

