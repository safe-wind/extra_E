# L’esercizio richiede di scrivere una funzione ricorsiva per sommare tutti gli elementi di un array.
# Ad esempio, per l’array [1, 2, 3, 4, 5], la funzione dovrebbe restituire 15.
# L’obiettivo è aiutare lo studente a comprendere come suddividere il problema in sottoproblemi più semplici, 
# facendo leva sulla riduzione dell’array fino alla sua dimensione minima.



def somma(num_list:list[int], lenght:int) -> int:

    if lenght <= 0:
        return 0
    else:
        return num_list[lenght-1] + somma(num_list, lenght-1)

                
print(somma([1, 5, 5, 5, 5],5))