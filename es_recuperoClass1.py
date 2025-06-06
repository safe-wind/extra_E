
class ContactManager:

    def __init__(self):
        self.contacts: dict[str,list[str]] = {}
    
    def create_contact(self, name:str, phone_numbers:list[str]) -> dict[str, list[str]]:
        """
        Documentazione della funzione
        """
        if name in self.contacts:
            raise ValueError("Contatto già esistente")
        else:
            self.contact[name] = phone_numbers
        
        return {name:phone_numbers} #
    
    def add_phone_number(self, contact_name:str, phone_number:str) -> dict[str, list[str]]:
        
        if contact_name not in self.contacts:
            raise ValueError("Errore contatto non è all'interno del dict")

        if phone_number in self.contacts[contact_name]:
            raise ValueError("contatto esiste già")
        
        self.contacts[contact_name].append(phone_number)
    
        
        return {contact_name : self.contacts[contact_name]}