#check value

def checkValue(num:int) -> str:
    if num > 5:
        print("The number is greater than 5")
    elif num < 5:
        print("The number is less than 5")
    else:
        print("The number is equal to 5")


checkValue(5)