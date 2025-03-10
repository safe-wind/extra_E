#es extra funzioni

#PAPER DOLL: Given a string, return a string where for
#every character in the original there are three characters

def charX3(word: str) -> str:

    new_word:list[str] = list()
    cont = 0

    while cont <= len(word)-1:

        for iter in word:

            if iter == word[cont]:
                new_word.append(iter*3)
                cont+=1

    new_word = "".join(new_word)
    return new_word

    
print(charX3("Lobby"))