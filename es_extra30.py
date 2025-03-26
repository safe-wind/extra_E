# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    par_a:int = 0
    par_c:int = 0
    output:bool = False

    for par in expression:

        if par=="(":
            par_a+=1

        elif par==")":
            par_c+=1

        else:
            output = False
            break

        if par_c == par_a:
            output=True
        elif par_a < par_c:
            output=False
            break
    return output
            
            

