#funzioni
#Scrivi una funzione che prende una lista di parole 
# e restituisce una lista contenente solo 
# le parole che iniziano con una lettera specificata.

parole_list: list[str] = list() #par1
lettera:str = input("Insert a letter to sort words that starts with the letter: ") #par2
lettera = lettera[0]
parole_toSort: list[str] = list() #par3

def sort_words(par1:list[str], par2:str, par3:list[str]):   #-> str

    for i in par1:

        if i[0]==str(par2):
            aggiunta:str = par3.append(i)
        else:
            continue
    return par3

            


while True:

    parole: str = input("Inserisci delle parole: ")
    parole_list.append(parole)

    if parole == "q":
        print("programma terminato.")
        break


print(sort_words(parole_list, lettera, parole_toSort))