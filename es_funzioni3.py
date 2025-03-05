#print numbers

def printNum(*par1:list[int]) -> int:

    for x in par1:

        print(x)

num_list:list[int] = [1, 2, 44, 3, 5]
printNum(*num_list)