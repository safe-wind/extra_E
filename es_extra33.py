#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(numbers:list[int]) -> int:
    isolati = 0

    for i in range(len(numbers)):

        if (i == 0 or numbers[i] != numbers[i-1]) and (i == len(numbers)-1 or numbers[i] != numbers[i+1]):
            isolati +=1 
    return isolati
   

print(count_isolated([1, 2, 3, 4, 5]))
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

        
