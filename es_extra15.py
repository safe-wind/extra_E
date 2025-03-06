#es 8 functions -(pynative.com)

#Find the largest item from a given list

# best method using built in function: max()
numbers: list[int] = [45, 68, 8, 24, 38, 2]
print(max(numbers))

#nfunction hand made
'''def largestNum(par1:list[int]) -> int:

    largest = None

    for element in par1:

        if largest == None:

            largest = element

        elif element > largest:

            largest = element

        else:
            continue

    return largest


print(largestNum([45, 68, 8, 24, 38, 2]))'''