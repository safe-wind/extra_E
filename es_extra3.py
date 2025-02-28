#funzioni
#Scrivi una funzione che prende una lista di numeri 
# e restituisce la somma di tutti gli elementi.

numeri:list[int] = list()

def somma(par1):

    sum= 0

    for i in range(0, len(par1)):
        sum+=i

    return sum

while True:

    num_inp: int = int(input("Insert number (-1 to quit):"))
    numeri.append(num_inp)

    if num_inp == -1 :
        print("Inserimento terminato.")
        break

    numeri_inp: int= int(input("Insert number (-1 to quit):"))
    numeri.append(num_inp)


total = somma(numeri)
print(f"La somma dei numeri è: {total}")

