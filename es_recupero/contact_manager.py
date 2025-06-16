
class ContactManager:

    def __init__(self, contacts:dict[str, list[str]]=None) -> None:

        if contacts is None:
            raise AttributeError("You have no contacts to manage!")
        else:
            self.contacts = contacts
    
    def create_contact(self, name:str, phone_numbers:list[str])-> None:

        if name in self.contacts.keys():
            print()
            raise ValueError("Errore: il contatto esiste già.")
        else:
            self.contacts[name] = phone_numbers
    
    def add_phone_number(self, contact_name:str, phone_number:str) -> dict[str, list[str]] | str:

        if contact_name not in self.contacts.keys():
            print()
            raise ValueError("Errore: il contatto non esiste.")
            
        elif phone_number in self.contacts[contact_name]:
            print()
            raise ValueError("Errore: il telefono esiste già.")
        
        else:
            self.contacts[contact_name].append(phone_number)
        
        return self.contacts
    
    def remove_phone_number(self, contact_name:str, phone_number:str) -> dict[str,list[str]]:

        if contact_name not in self.contacts:
            print()
            raise ValueError("Errore: il contatto non esiste.")
            
        elif phone_number not in self.contacts[contact_name]:
            print()
            raise ValueError("Errore: il telefono non è presente.")
        
        else:
            self.contacts[contact_name].remove(phone_number)

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str)-> dict[str,list[str]]: 
        if contact_name not in self.contacts:
            print()
            raise ValueError("Errore: il contatto non esiste.")
            
        elif old_phone_number not in self.contacts[contact_name]:
            print()
            raise ValueError("Errore: il telefono non è presente.")
        
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
    
    def list_contacts(self) -> list[str]:

        return list(self.contacts.keys())

    def list_phone_number(self, contact_name:str) -> list[str]:

        if contact_name not in self.contacts:
            print()
            raise ValueError("Errore: il contatto non esiste.")
            
        else:
            return self.contacts[contact_name]
        
    def search_contact_by_phone(self, phone_number:str) -> list[str]:

        lista_contatti_phonenumb:list = list()

        for contatto in self.contacts.keys():

            if phone_number in self.contacts[contatto]:

                lista_contatti_phonenumb.append(contatto)
            else:
                ValueError("Nessun contatto trovato con questo numero")
                
        return lista_contatti_phonenumb

