
#es_parentesi
'''
caso1:str = "((()))"
caso2:str = "(()"
caso3:str = "()()()"
caso4:str = "))(("
caso5:str = "(()())"
'''
print("Scrivi una serie di parentesi:")

caso = input(str(""))

#inizializzo la variabile output a false in caso la stringa sia vuota
# e inizio 2 contatori di caratteri nella stringa

par_a:int = 0
par_c:int = 0
output:bool = False

# Itero nella stringa e incremento 
# un contatore ogni volta che si incontra 
# una par_a o par_c

for par in caso:

    if par=="(":
        par_a+=1

    elif par==")":
        par_c+=1

# se i caratteri sono diversi da  "(" o  ")",
# finisce il ciclo

    else:
        output = False
        break

# sempre nel ciclo verifico se ci sono sbilanciamenti tra le par_a e le par_c
# se sono uguali sono bilanciate e output è True 
# ma se le par_a vengono dopo le par_c nell'iterazione allora l'output è False e interrompo il ciclo

    if par_c == par_a:
        output=True
    elif par_a < par_c:
        output=False
        break
        

print(output)
