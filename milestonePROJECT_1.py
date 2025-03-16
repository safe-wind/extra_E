# Create a Tic Tac Toe game.

# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


#Clear output

def clearOutput() -> None:
    print("\n"*10)

#Definisco una funzione per iniziare il gioco

def startGame() -> str:

    while True:
        start = input("Do you want to play Tris?: (enter 'start' to play) ('stop' to end) ")

        if start == 'stop':
            print('Game offline')
            break

        elif start == 'start':
            print("\n"*10)
            print('Game started succesfully.')
            print()
            break
            
        else:
            print(f'Sorry you didn\'t choose the correct option. Try again ')
    return start

#definisco una funzione che stampa la tabella del gioco
def tableGame(pos:list[str]) -> None:
    
    print(f"{pos[0]}" + "|" + f"{pos[1]}" + "|" + f"{pos[2]}") 
    print("_" + "|" + "_" + "|" + "_" + " ")
    print(f"{pos[3]}" + "|" + f"{pos[4]}" + "|" + f"{pos[5]}") 
    print("_" + "|" + "_" + "|" + "_" + " ")
    print(f"{pos[6]}" + "|" + f"{pos[7]}" + "|" + f"{pos[8]}")

#definisco uma funzione dove chiedo ai giocatori di scegliere 'X' o 'O'
def playerInput() -> str:

    while True:
        player1:str = input("Player1: Choose 'X' or 'O': ").upper()
        
        print("\n"*5)

        if player1 == 'X':
            player2 = 'O'
            print("Player1 is 'X'")
            print("Player2 is 'O'")
            print()
            break
            
        elif player1 == 'O':
            player2  = 'X'
            print("Player1 is 'O'")
            print("Player2 is 'X'")
            print()
            break

        elif player1 not in ['X', 'O']:
            print("Sorry you didn't choose a correct option")

    return player1, player2

#definisco una funzione dove il player sceglie la posizione da 1 a 9
# e in base al giocatore che sceglie, il marker va inserito nella displayTable

def gameStarted(table, player1, player2):
    cont = 0
    while cont < 9:

        pos1 = abs(int(input("Player1 :Scegli dove mettere il marker (1-9): ")))
        clearOutput()
    #inserisco il segno nella posizione indicata da 1 a 9
        match pos1:
            
            case 1:
                table.pop(0)
                table.insert(0, player1)
            case 2:
                table.pop(1)
                table.insert(1, player1)
            case 3:
                table.pop(2)
                table.insert(2, player1)
            case 4:
                table.pop(3)
                table.insert(3, player1)
            case 5:
                table.pop(4)
                table.insert(4, player1)
            case 6:
                table.pop(5)
                table.insert(5, player1)
            case 7:
                table.pop(6)
                table.insert(6, player1)
            case 8:
                table.pop(7)
                table.insert(7, player1)
            case 9:
                table.pop(8)
                table.insert(8, player1)
            case _:
                pass
        cont+=1
        tableGame(table)
        if cont == 9:
            break


        
        pos2 = abs(int(input("Player2 :Scegli dove mettere il marker (1-9): ")))
        clearOutput()

        match pos2:
            
            case 1:
                table.pop(0)
                table.insert(0, player2)
            case 2:
                table.pop(1)
                table.insert(1, player2)
            case 3:
                table.pop(2)
                table.insert(2, player2)
            case 4:
                table.pop(3)
                table.insert(3, player2)
            case 5:
                table.pop(4)
                table.insert(4, player2)
            case 6:
                table.pop(5)
                table.insert(5, player2)
            case 7:
                table.pop(6)
                table.insert(6, player2)
            case 8:
                table.pop(7)
                table.insert(7, player2)
            case 9:
                table.pop(8)
                table.insert(8, player2)
            case _:
                pass
        cont+=1
        tableGame(table)
        if cont == 9:
            print("\n"*10)
            checkWinLosePair(table, player1, player2)
            break


def checkWinLosePair(table, player1, player2):


    match table:
        case table if table[0] == table[1] == table[2]: #casi orizzontali
            print(f"{player1 or player2} wins!")
        case table if table[3] == table[4] == table[5]:
            print(f"{player1 or player2} wins!")
        case table if table[6] == table[7] == table[8]:
            print(f"{player1 or player2} wins!")
        case table if table[0] == table[3] == table[6]: #caso tris verticale a sinistra
            print(f"{player1 or player2} wins!")
        case table if table[1] == table[4] == table[7]: #caso tris verticale centro
            print(f"{player1 or player2} wins!")
        case table if table[2] == table[5] == table[8]: #caso tris verticale destra
            print(f"{player1 or player2} wins!")
        case table if table[0] == table[4] == table[8]: #caso diagonale da sx a dx
            print(f"{player1 or player2} wins!")
        case table if table[2] == table[4] == table[6]: #caso diagonale da dx a sx
            print(f"{player1 or player2} wins!")
        case _:
            print("Pair!")

        
#creo una lista dove ci vanno tutti i marker del gioco 
table:list[str] = []

# Test tabella visual
table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# tableGame(markers)

#programma Tris

while True:
    table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print()
    print("----------------------- WELCOME IN TRIS! -------------------------")
    print()
    #inizio del gioco
    status = startGame()
    if status == "stop":
        break
    else:   
    #scelta di 'X' o 'O'

        player1, player2 = playerInput()
        
        gameStarted(table, player1, player2)
        checkWinLosePair(table,player1,player2)
