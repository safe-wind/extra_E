

def countDown(n:int) -> None:
    if n < 0:
        print("errore")
    
    elif n == 0:
        print(0)
        
    else:    
        print(n)
        countDown(n-1)
    

countDown(6)