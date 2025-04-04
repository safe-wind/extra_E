# Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista. 
# Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.
# Il tuo compito è individuare i numeri mancanti.
# Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente tutti i numeri 
# da 1 a n che non sono presenti nella lista originale.

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    new_list = list()

    for i in range(1, n+1):

        if i not in nums:
            
            new_list.append(i)
    
    return new_list

print(find_disappeared_numbers([1,8,9,150]))