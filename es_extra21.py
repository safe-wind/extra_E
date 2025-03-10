#es extra funzioni 

#BLACKJACK: Given three integers between 1 and 11,
#if their sum is less than or equal to 21, 
#return their sum. 
# If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10.
# Finally, if the sum (even after adjustment) 
# exceeds 21, return 'BUST'

def blackjack(n1:int, n2:int, n3:int) -> None:

    somma = n1 + n2 + n3

    if n1 == 11 or n2 == 11 or n3 == 11:
        somma = somma - 10
    
    match somma:

        case somma if somma >=1 and somma <= 21:
            result = print(f"sum is: {somma}")

        case somma if somma > 21:
            result = print("you got: BUST")

        case _:
            result = print("Impossible")
            

blackjack(5,11,10)

