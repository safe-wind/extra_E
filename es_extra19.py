#es extra funzioni

#Given a list of ints, return True if the array
#contains a 3 next to a 3 somewhere.

def has3next3(numbers:list[int]) -> bool:

    flag:bool = False

    for number in range(len(numbers)-1):

        if numbers[number] == 3:

            if numbers[number+1] == 3:

                flag = True
                break

            else:
                continue

        else:
            flag = False
        
            
    return flag


print(has3next3([1, 3, 3, 1, 3]))