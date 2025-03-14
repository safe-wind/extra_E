#esercizio 6 compito

#Scrivere un programma che acquisisca 
# in input due numeri interi, n1 e n2, 
# e calcoli il prodotto di tutti i numeri 
# compresi tra n1 e n2, inclusi gli estremi.


n1:int = int(input("Inserire primo numero: "))
n2:int = int(input("Inserire secondo numero: "))
prodotto = 1

if n1 > n2:

    for num in range(n1, n2+1, 1):
        prodotto = n1*n2
        n1+=1
    print(f"Il prodotto è {prodotto}")

else:

    for num in range(n2, n1-1, -1):
        prodotto *= n2
        n2 -=1
    print(f"Il prodotto è {prodotto}")

    