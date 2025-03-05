#es 6 funzioni - pynative.com

'''def sommaValues(par1:int, par2:int) ->int:

    somma = 0

    for i in range(par1, par2 + 1):

        somma+=i
    
    return somma

print(sommaValues(0, 10))'''

# Write a program to create a recursive function 
# to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls
# itself again and again.

def addValues(num:int) -> int:

    if num:
        add = num + addValues(num-1)
        return add
    
    else:
        return 0


print(addValues(10))