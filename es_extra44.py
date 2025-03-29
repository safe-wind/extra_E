# La funzione deve calcolare il resto della divisione tra due numeri senza usare l’operatore %. 
# Ad esempio, per 17 ÷ 5, il risultato sarà 2.
# Questo esercizio è utile per comprendere come la sottrazione iterativa possa simulare l’operazione di modulo, 
# senza fare affidamento su operatori già pronti.

def divResto(n1:int, n2:int) -> int:

    if n1 < n2 : 
        return n1
    else:
        return divResto(n1-n2, n2)


print(divResto(17, 5))