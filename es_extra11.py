#es 5 functions (pynative.com)

# Create an outer function that will accept 
# two parameters, a and b Create an inner 
# function inside an outer function that 
# will calculate the addition of a and b
# At last, an outer function will add 5 
# into addition and return it

def values(a:float, b:float) -> float:

    somma:float = a + b
    #incrByFive(somma)

    return somma+5

#def incrByFive(arg1: float) -> float:

    #somma_incr:float = arg1+5

    #return somma_incr

print(values(10.5, 5.5))