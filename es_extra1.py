#es12 loop pynative

num1 = 0

num2 = 1

risultato = 0

for i in range(1, 11):

    risultato = num1+num2

    num1 = num2

    num2 = risultato

    print(risultato)
