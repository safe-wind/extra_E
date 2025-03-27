#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(numbers:list[int]) -> int:
    isolati = 0

    for i in range(len(numbers)):
        #print(i)
        #il primo e ultimo numeri sono isolati  se non hanno alla loro destra o sinistra un numero uguale

        if numbers[i] == numbers[i+1]:
            continue
        elif numbers[i] == numbers[i-1]:
            continue

        if numbers[i] != numbers[i-1]:
            isolati +=1 
            
        elif numbers[i] != numbers[i-1] and numbers[i+1]:
            isolati +=1
        

    return isolati
   

print(count_isolated([1, 2, 3, 4, 5]))
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

        
