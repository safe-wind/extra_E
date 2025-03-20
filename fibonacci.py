

def fibonaccio(n:int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return int(fibonaccio(n-1)+fibonaccio(n-2))
    

print(fibonaccio(6))