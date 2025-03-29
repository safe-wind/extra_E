# Questa funzione verifica se un array è ordinato in ordine crescente. Se l’input è [1, 2, 3, 4, 5], 
# la funzione restituisce true, mentre per [1, 3, 2, 4, 5] restituisce false.
#L’esercizio è utile per far capire come la ricorsione possa essere utilizzata per analizzare 
# progressivamente coppie di elementi, senza dover esaminare l’intero array in un solo passaggio.

def ordinato(arr:list[int], dim:int) -> bool:
    if dim <= 1:
        return True  # Un solo elemento è sempre ordinato
    if arr[dim - 2] > arr[dim - 1]:
        return False  # Se l'elemento precedente è maggiore del successivo, non è ordinato
    return ordinato(arr, dim - 1)  # Verifica ricorsivamente il resto dell'array