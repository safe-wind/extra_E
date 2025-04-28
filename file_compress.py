def memorizza_file(file_sizes):
    blocchi_disponibili = 1000
    

    for size in file_sizes:
        compresso = size * 0.8

        blocchi_necessari = round(compresso / 512)  
        
        if blocchi_necessari <= blocchi_disponibili:
            blocchi_disponibili -= blocchi_necessari
            print(f"File di {size} byte compresso in {compresso:.1f} byte e memorizzato. "
                  f"Blocchi usati: {blocchi_necessari}. Blocchi rimanenti: {blocchi_disponibili}.")
        else:
            print(f"Non è possibile memorizzare il file di {size} byte. Spazio insufficiente.")
            


memorizza_file([1100, 20000, 1048576, 512, 5000])
memorizza_file([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])