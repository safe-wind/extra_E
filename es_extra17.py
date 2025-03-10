#es yoda

# MASTER YODA: Given a sentence, return a
# sentence with the words reversed

def master_yoda(sentence:str) -> str:
                                        #creo una lista vuota dove andrò ad inserire gli elementi della "sentence"

    new_sentence:list[str] = []

                                        #con .split() isolo singolarmente gli elementi del sentence 
    sentence_list:list[str] = sentence.split() 

                                        #con un ciclo vado ad iterare dall ultimo elemento al primo
                                        #inserendoli in una nuova lista con il nuovo ordine (inverso)
    for elements in sentence_list[::-1]:

        new_sentence.append(elements)

                                        #poi return della nuova frase   
    return new_sentence

                                        #con l'operatore asterisco considero gli elementi della lista 
                                        #singolarmente
print(*master_yoda("I am home"))