#  Scrivi una funzione che, dato un numero intero,
#  determina se è un "numero magico". Un numero magico è
#  definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:

    num_string = str(num)
    magic_num = None

    if len(num_string) > 1:

        for i in num_string:
            if i == "7":
                magic_num = True
                break
            else:
                magic_num = False
    elif len(num_string) == 1:

        if num_string == "7":
            magic_num = True
        else:
            magic_num = False
    else:
        magic_num = False

    return magic_num
            
