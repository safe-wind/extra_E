#es_parentesi

domanda:str = "Inserisci una serie di parentesi e verifica se sono bilanciate: "
print(domanda)
parentesi:str = input(str())

count_par = 0
output = True

for par in parentesi:

    if par=="(":

        count_par += 1

    elif par==")":

        count_par -= 1

    if count_par < 0 or count_par>0:
        output=False
        break

print(output)
    


    
    
        

        