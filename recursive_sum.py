

def recSum(n:int) -> None:
    
    if n < 0:
        return print("Errore")
    
    elif n == 0 :
        return print(0)
  
    else:
        somma = 0
        while n:
            somma = somma + n
            n = n-1

        return somma
            


print(recSum(5))
