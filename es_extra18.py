#es extra funzioni

#Given an integer n, return True 
# if n is within 10 of either 100 or 200

def almost_there(num:int) -> bool:

    flag:bool = False

    match num:

        case num if num >= 90 and num<= 110:
            flag = True
        case num if num >= 190 and num <= 210:
            flag = True
        case _:
            flag = False
    
    return flag


while True:

    num: int = abs(int(input("Inserisci un numero tra 100 e 300: ")))

    if num > 0:
        break


print(almost_there(num))