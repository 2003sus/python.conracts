import numbers

 
 
#line 83,76,70


class Contacts:
    
    list_of_contacts = []
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.list_of_contacts.append(self)




class Functions:
    
    
    def create_accounts(name,phone_number): 
        new_contact = Contacts(name.lower(),phone_number.lower())       
        
    def read_contacts():
        if Contacts.list_of_contacts == []:
            print("NO contacts at the moment!")
            
        for contact in Contacts.list_of_contacts:
            print(f"name:{contact.name}  number:{contact.phone_number}\n")
            
            
    def delete_contact():
        while True:
            print("Delete all contacts PLz enter 0:\n Delete individual ones plz enter 1:  ")  
            choice_of_delete = input("Here>>")
            if choice_of_delete == "0":
                Contacts.list_of_contacts.clear()
                print("deleted all contacts successfully !! ") 
                break
            elif choice_of_delete == "1":
                print("plz Enter the name and the number of the person that you want to delete")
                Deleting_specific_individual_name   = input("name:  ").lower()
                Deleting_specific_individual_number = input("number:  ").lower() 
                if len(Contacts.list_of_contacts) != 0:
                    
                    for contact in Contacts.list_of_contacts:
                        if contact.name == Deleting_specific_individual_name and contact.phone_number == Deleting_specific_individual_number:
                            Contacts.list_of_contacts.remove(contact)  
                            print("deleted successfully !! ") 
                            break
                            
                            
                        print("NO such contact found PLz try again")
                           
                    break
                else:
                    print("there are no contacts at the moment")  
                    break 
            else:     
                print("Wrong Input!! PLz try again")            
    def updating_contact():
       
            print("plz Enter the name and the number of the person that you want to update with  ")
            Deleting_specific_individual_name   = input(" name  >").lower()
            Deleting_specific_individual_number = input("number  >").lower()
            if len(Contacts.list_of_contacts) != 0:
                    for contact in Contacts.list_of_contacts:
                        
                                if contact.name == Deleting_specific_individual_name and contact.phone_number == Deleting_specific_individual_number: 
                                    print(f"Modify the name  {contact.name}  click 1 :""\n")
                                    print(f"Modify the number  {contact.phone_number}  click 2 :""\n")
                                    print(f"Modify all {contact.name  }  and {contact.phone_number}  click 0 :")
                                    Choice_of_name_and_number = input("Here>>")
                                    if Choice_of_name_and_number == "1":
                                        new_name = input("Enter the new name>>")
                                        contact.name = new_name
                                        print("updated successfully!")
                                        break
                                    elif Choice_of_name_and_number == "2":
                                        new_name = input("Enter the new number>>")
                                        contact.phone_number = new_name  
                                        print("updated successfully!")
                                        break  
                                    elif Choice_of_name_and_number == "0":
                                        new_name = input("Enter the new name>>")
                                        new_number = input("enter the new number>>")
                                        contact.name = new_name 
                                        contact.phone_number = new_number 
                                        print("updated successfully!")
                                        break
                                    else:
                                        print("Wrong input Plz try again")    
                                print("no Such contact")        
                                    
                        
def main():
    while True:
        print("\n \n   <<Contact Archive>> ") 
        print("\n<< Create new contacts >>   1 ")
        print("<< Read contacts >>         2 ")  
        print("<< Delete contacts >>       3 ")
        print("<< Update contacts >>       4 ")   
        print("   press * to terminate    ")
        The_choice = input("Enter the perspective number corresponding to the function>>") 
        if The_choice == "1":
            print("pending...")
            new_name = input("name: ")
            new_number = input("number: ")
            Functions.create_accounts(new_name,new_number)  
            print("created successfully !")             
        elif The_choice ==   "2":
            Functions.read_contacts()           
        elif The_choice == "3":
            Functions.delete_contact()
        elif The_choice == "4":
            Functions.updating_contact()    
        elif The_choice == "*":
            print(" Have a great one!")
            break    
        else:
            print("Incorrect input Plz try again!")    
            
main()            