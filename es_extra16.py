#LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes
# the first and fourth letters of a name
# Expected output: 
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'


def capitalize1_4(word:str) -> str:

    new_word:list[str] = list(word)

    for parola in new_word:

        for letter in parola:

            new_word[0] = letter.upper()
            lettera1 = new_word[0]
            new_word[3] = letter.upper()
            lettera4 = new_word[3]
            return lettera1
        return lettera4    
    return "".join(new_word)

print(capitalize1_4("macdonald"))





    