# Si chiede di calcolare la somma dei primi N numeri naturali. Ad esempio, con N = 4, 
# la funzione restituisce 10 perché 1 + 2 + 3 + 4 = 10.
# L’obiettivo è insegnare il concetto di accumulazione in una funzione ricorsiva, 
# facendo leva su una chiamata ridotta per ogni passo.

def sommaN(n:int) -> int:
    if n <= 0:
        return 0
    elif n < 2:
        return 1
    else:
        return n + sommaN(n-1)
    
print(sommaN(4))
