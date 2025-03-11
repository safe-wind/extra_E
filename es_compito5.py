#es compito 5

# Si supponga di poter acquistare barrette di
# cioccolato da un distributore automatico al 
# costo di 1 euro ciascuna. Ogni barretta
# acquistata contiene un buono sconto, 
# e con 6 buoni sconto si ottiene una barretta 
# gratuita.


buoni_rim=0

while True:

    num_barrette = int(input("Inserisci euro disponibili: "))
    num_barrette += buoni_rim
    barrette_totali = num_barrette + (num_barrette/6)
    
    print("Puoi comprare ",int(barrette_totali)," barrette")

    acquisto = int(input("Quante barrette vuoi acquistare?: "))

    print("Hai acquistato ",acquisto," barrette")

    buoni_rim = barrette_totali - acquisto
    buoni_rim = buoni_rim % 6

    print(f"Ti rimangono {int(buoni_rim)} buoni")
    
    
        



