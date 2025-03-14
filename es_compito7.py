#es 7 compito

# Scrivere un programma che inizializzate 
# due liste a e b della stessa lunghezza n,
# entrambe contenenti valori interi, 
# calcoli la somma incrociata degli elementi.

a:list[int] = [1, 2, 3, 4, 5]
b:list[int] = [5, 4, 3, 2, 1]

c:list[int] = []
somma = 0

for iter0 in range(0, len(a), 1):

    for iter1 in range(len(b)-1, 0 , -1):

        somma= a[iter0] + b[iter1]
        c.append(somma)
        
    

print(c)



