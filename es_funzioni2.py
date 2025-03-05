#check lenght

def checkLenght(par1:str) -> str:

    if len(par1) > 10:
        print(f"Lenght of the string \"{par1}\" is greater than 10")
    elif len(par1) < 10:
        print(f"Lenght of the string \"{par1}\" is less than 10")
    else:
        print(f"Lenght of the string  \"{par1}\" is equal to 10")

checkLenght("california")