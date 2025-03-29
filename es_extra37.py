# Si chiede di scrivere una funzione ricorsiva che stampi i numeri da 1 a N,
#  ignorando i casi in cui N sia minore di 1.
#  Se N = 5, l’output sarà 1 2 3 4 5.
# L’obiettivo didattico è mostrare come la ricorsione possa sostituire un ciclo iterativo, 
# gestendo la progressione dei numeri attraverso chiamate successive.

def stampa_valori(n):

    if n <= 0:
        pass  # Se n è minore o uguale a 0, non fare nulla
    else:
        stampa_valori(n - 1)  # Chiamata ricorsiva con n-1
        print(n)

            
    
stampa_valori(5)