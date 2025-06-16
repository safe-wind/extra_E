
x:int = int(input("Numero intero positivo x: "))
seq_num:list[int] = list()
conteggio_elem:dict[str] = {}

while True:
    num:int = int(input("Inserisci dei numeri in sequenza: "))

    if num > 0:
        seq_num.append(num)
    else:
        break

print(seq_num)


