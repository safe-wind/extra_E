#es 8 functions - pynative.com

# Generate a Python list of all the even
# numbers between 4 to 30

# more efficient method using built in function: range()

print(list(range(4, 30, 2)))

# other method slicing
'''numbers:list[int] = list(range(30))

print(numbers[4:30:2])'''

# function hand made
'''def rangeEven(par1:int) -> list[int]:

    even_list: list[int] = list()

    for element in range(4, par1):

        if element%2==0:

            even_list.append(element)
        
        else:
            continue

    return even_list

print(rangeEven(30))'''