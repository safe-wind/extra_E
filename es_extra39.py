

def recursiveCounter(n:int) -> int:

    if abs(n) < 10:
        return 1
    else:
        return abs(1+recursiveCounter(n // 10))
    
print(recursiveCounter(120))
print(recursiveCounter(-9000))