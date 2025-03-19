

def recursiveSumInRange(a:int, b:int) -> int:

    if a > b :

        temp = a

        a = b
        b = temp
        #a, b = b, a

    if b==a :
        return a
    else:
        

        return int(b + recursiveSumInRange(a, b-1))