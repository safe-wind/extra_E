# Scrivi una funzione che accetti tre parametri: 
# username, password e status di attivazione dell'account (attivo/non attivo).
#  L'accesso è consentito solo se il nome utente è "admin",la password corrisponde a "12345" e l'account è attivo. 
#  La funzione ritorna "Accesso consentito" oppure "Accesso negato".

def check_access(username: str, password: str, is_active: bool) -> str:
    access_dict = {
        "username":username.lower(),
        "password":password,
        "is_active":is_active
    }
    
    if access_dict == {"username":"admin", "password":"12345", "is_active":True}:
        return "Accesso consentito"
    
    else:
        return "Accesso negato"