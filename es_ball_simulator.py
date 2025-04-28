# Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra 
# in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

# Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

# Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza 
# il valore della velocità corrente; poi, il valore della velocità viene modificato, 
# sottraendo 96 al valore della velocità corrente.
# Dunque, dopo ogni secondo, si ha che
# altezza = altezza + velocità
# velocità = velocità - 96.
 
# Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 
# per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
# altezza= altezza*-0,5 
# velocità=velocità*-0,5.

# Ci si fermi al quinto rimbalzo.
 
# Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in 
# quel determinato secondo.
# Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
# "Tempo: 0 Altezza: 0"
 
# Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
# Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
# "Tempo: 4 Rimbalzo!"

#tempo = 0 -> altezza = 0 -> velocita  = 100 cm/s
#tempo = 1 -> altezza = altezza + velocita   -> velocita = velocita- 96 cm/s
# if altezza < 0 -> altezza *= -0.5 & velocita *= -0.5
# 5 rimbalzo stop!
def rimbalzo():
    tempo = 0
    altezza = 0.0
    velocita = 100.0
    rimbalzi = 0

    while rimbalzi < 5:
        
        if altezza < 0:
            altezza *= -0.5
            velocita *= -0.5
            print(f"Tempo: {tempo} Rimbalzo!")
            rimbalzi += 1
            tempo += 1
        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")
            altezza += velocita
            velocita -= 96    
            tempo +=1

rimbalzo()
