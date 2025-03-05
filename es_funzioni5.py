#es 5

def addOne(par1:int) -> int: #funzione1

    add = par1 + 1

    return add

def addOneToList(par2:list[int]) -> list[int]: #funzione2

    new_list: list[int] = list()

    for element in par2:

        value_incr = addOne(element)
        new_list.append(value_incr)
    
    return new_list

print(addOneToList([1, 2, 3]))

        
