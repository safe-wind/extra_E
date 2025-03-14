#es 8 compito 

#Un'applicazione interessante dei computer è 
# la rappresentazione grafica di dati.
#Scrivere un programma che acquisisca cinque
#  numeri interi (ognuno compreso tra 1 e 30)
#  e visualizzi in output un grafico a barre 
# testuale con asterischi *

i = 0 #cont. ciclo while
num:list[int] = []

while i < 5:

    numbers:int = int(input("Inserisci un numero tra 1 e 30: "))
    num.append(numbers)
    i+=1

for number in num:

    for x in range(0, number):
        print("*", end = "")
    print()
