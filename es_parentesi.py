
bilanciate:str = input(str())

open_par = 0
close_par = 0
output = True

for par in bilanciate:

    if par=="(":
        open_par += 1
    elif par==")":
        close_par += 1
    else:
        output = False
        break

    if close_par <= open_par:
        output= True
    elif close_par > open_par:
        output= False
    
    
        
if open_par==close_par:
    print(output)
else:
    print(output)