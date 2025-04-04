
# Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 inclusi.

# Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
# Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
# L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
# Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere 
# considerato 1 per evitare il "bust" (superare 21).
# Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle 
# carte e restituisce il valore totale della mano secondo le regole del Blackjack.


def blackjack_hand_total(cards: list[int]) -> int:
    points = 0

    if sum(cards) > 21:
        if 11 not in cards:
            print("Bust")
            return points + sum(cards)
        elif 11 in cards:
            
            return points + sum(cards)-10
        
    elif sum(cards) < 21:
        if 1 not in cards:
            return points + sum(cards)
        
        elif 1 in cards:
            return points + sum(cards)+10

    
    if sum(cards) == 21:
        return points + sum(cards)

    


print(blackjack_hand_total([2, 3, 5]))
print(blackjack_hand_total([11, 6, 5]))
