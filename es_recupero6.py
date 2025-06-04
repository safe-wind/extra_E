# Scrivere in Python dei cicli che stampino le 
# seguenti sequenze di valori:
# a) 2, 4, 6, 8, 10, 12, 14
# b) 1, 4, 7, 10, 13
# c) 30, 25, 20, 15, 10, 5, 0
# d) 5, 15, 25, 35, 45

def ciclo_a() -> None:
    for a in range(2,15, 2):
        print(a)

def ciclo_b() -> None:
    for b in range(1,14, 3):
        print(b)

def ciclo_c() -> None:
    for c in range(30,-2, -5):
        print(c)

def ciclo_d() -> None:
    for d in range(5,49,10):
        print(d)
print("Ciclo A")
ciclo_a()
print("Ciclo B")
ciclo_b()
print("Ciclo C")
ciclo_c()
print("Ciclo D")
ciclo_d()