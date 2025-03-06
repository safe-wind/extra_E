#LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes
# the first and fourth letters of a name
# Expected output: 
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'

#metodo slicing

def capitalize1_4(word:str) -> str:

#divido la stringa nelle parti che mi interessano:

    letter1 = word[0].upper()  #prima lettera della stringa
    letter2to3 = word[1:3]     #seconda e terza lettera
    letter4 = word[3].upper()  #quarta lettera 
    rest_of_letters = word[4:] #quinta lettera in poi

#sommo tutte le variabili che compongono la stringa
    return letter1 + letter2to3 + letter4+ rest_of_letters

print(capitalize1_4("macdonald"))





    