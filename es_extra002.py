

def prime_factors(n:int) -> list[int]:

    num_primo = list()
    div = 2

    while n>1:
        if n%div == 0:
            n//=div
            num_primo.append(div)
        else:
            div += 1
    return num_primo

print(prime_factors(622919))