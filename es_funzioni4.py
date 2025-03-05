#check each

def checkEach(list:int) -> str:

    for element in list:

        if element > 5:
            print(f"Number {element} is bigger than 5")

        elif element < 5:
            print(f"Number {element} is less than 5")

        else:
            print(f"Number {element} is equal to 5")

list_num: list[int] = [1, 5, 7]
checkEach(list_num)