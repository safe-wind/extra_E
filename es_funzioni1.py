#es funzione


def somma_funzione(a:int, b:int):
    sum: int= 0
    for i in range(a, b+1):
        sum+=i

    return sum

print(somma_funzione(1, 10))
print(somma_funzione(20, 37))
print(somma_funzione(35, 49))