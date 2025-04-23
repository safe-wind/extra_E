# PARTE 1
# Scrivi una funzione chiamata create_contact() che accetta il nome e 
# cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
# La funzione dovrebbe restituire un dizionario con i dettagli del 
# contatto.
 
# PARTE 2
# Scrivi una funzione chiamata update_contact() che accetta il 
# dizionario creato, il nome e cognome del contatto da aggiornare, e 
# il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe 
# aggiornare il dizionario del contatto.
# For example:

# Test	Result
# contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
# print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
# print(update_contact(contact, "Mario Rossi", telefono=123456789))

def create_contact(nome:str, email:str=None, telefono:str=None):
    return {
        'profile': nome,
        'email': email,
        'telefono': telefono
    }

def update_contact(contatto, nome:str, email=None, telefono=None):
    
    if contatto['profile'] != nome:
        return contatto  

    if email is not None:
        contatto['email'] = email
    if telefono is not None:
        contatto['telefono'] = telefono

    return contatto

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(contact)
updated = update_contact(contact, "Mario Rossi", telefono=123456789)
print(updated)