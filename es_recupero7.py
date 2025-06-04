# funzione che scrive un fattoriale di un numero n

def fattoriale(n:int) -> int:

    prodotto_cumulato = 1
    if n == 1:
        return n
    else:
        while n > 0:

            prodotto_cumulato*=n
            n-=1

    return prodotto_cumulato

print(fattoriale(10))
