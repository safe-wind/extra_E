from string import ascii_lowercase
#chiave:num int pos, incrementa l'indice che 
#corrisponde a un altra lettera dell'alfabeto

def caesar_cypher_encrypt(s:str, k:int) -> str:
    
    s = s.lower()
    alfabeto :str = ascii_lowercase

    if k > 26:
        k = k%26

    crypted_s = "" 

    for indice in range(len(s)):
        if s[indice] in alfabeto:
            posiz = alfabeto.index(s[indice])
            posiz_cryptata = (posiz+k) % 26

            crypted_s += alfabeto[posiz_cryptata]
        #se spazio o carattere speciale
        else:
            crypted_s += s[indice]

    return crypted_s


def caesar_cypher_decrypt(s:str, k:int) -> str:
    
    s = s.lower()
    alfabeto :str = ascii_lowercase

    if k > 26:
        k = k%26

    decrypted_s = "" 

    for indice in range(len(s)):
        if s[indice] in alfabeto:
            posiz = alfabeto.index(s[indice])
            posiz_decryptata = (posiz-k) % 26

            decrypted_s += alfabeto[posiz_decryptata]
        #se spazio o carattere speciale
        else:
            decrypted_s += s[indice]

    return decrypted_s

stringa1 = "Ciao"

print(caesar_cypher_encrypt(stringa1, k= 4))
print(caesar_cypher_decrypt("gmes",k =4))