#funzioni
#Scrivi una funzione che prende una lista di numeri 
#e restituisce una lista contenente solo i numeri pari.

num_temp:list[int] = list() 
num_final: list[int] = list() #par1

def numeri_pari(par1:list[int]): #-> list[int]

    return par1

num_inp: int = int(input("inserisci un numero: (-0 to quit) "))
num_temp.append(num_inp)

while True:
    if not num_inp == 0 :
        num_inp: int = int(input("inserisci un numero: (-0 to quit) "))

        if num_inp % 2 == 0:
            num_final.append(num_inp)
        else:
            num_temp.append(num_inp)
        
    else:
        print("Programma terminato")
        break

print(num_temp)

print(numeri_pari(num_final))
