#program to write contact book
class Contact:
    def _init_(self, name, phone_number,email,address):
        self.name = name
        self.phone_number = phone_number
        self.email=email
        self.address=address

class ContactBook:
    def _init_(self):
        self.contacts = []


    #Function to add contacts
    def add_contact(self, contact):
        self.contacts.append(contact)


    #Function to display contacts
    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")


    #Function to search conatcts         
    def search_contacts(self,name):
        matching_contacts=[contact for contact in self.contacts if contact.name.lower()==name.lower()]
        return matching_contacts

     #Function to Update contacts
    def update_contacts(self,name,new_phone_number,new_email,new_address):
        contact=next((contact for contact in self.contacts if contact.name.lower()==name.lower()),None)
        if contact:
            contact.phone_number=new_phone_number
            contact.email=new_email
            contact.address=new_address
        else:
            print("contact not found")
            

    #Function to delete contacts        
    def delete_contacts(self,name):
        contact=next((contact for contact in self.contacts if contact.name.lower()==name.lower()),None)
        if contact:
            self.contacts.remove(contact)
        else:
            print("contact not found")


#Main function         
def main():
    contact_book = ContactBook()
    while True:
        print("1. Add contact")
        print("2. Display contacts")
        print("3.search contacts")
        print("4.Update contacts")
        print("5.Delete contacts")
        print("6. Exit")
        
        #prompt the user to input 
        option = int(input("Enter your option: "))
        if option == 1:
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email=input("Enter email: ")
            address=input("Enter address: ")
            contact = Contact(name, phone_number,email,address)
            contact_book.add_contact(contact)
        elif option == 2:
            contact_book.display_contacts()
        elif option == 3:
            name=input("Enter name to search: ")
            contacts=contact_book.search_contacts(name)
            if contacts:
                for contact in contacts:
                    print(f"{contact.name}: {contact.phone_number}")
            else:
                print("contact not found")
        elif option == 4:
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email=input("Enter new email id: ")
            new_address=input("Enter new address: ")
            contact_book.update_contacts(name, new_phone_number,new_email,new_address)
        elif option == 5:
            name = input("Enter name to delete: ")
            contact_book.delete_contacts(name)
        elif option == 6:
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()