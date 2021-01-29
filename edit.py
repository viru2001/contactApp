import sqlite3
from db_helper import update
from helper_functions import isContactSaved,isValidPhoneNumber

def edit(name):
    db = sqlite3.connect("contacts.db")
    
   
    if isContactSaved(db,name):
        whatToEdit = input("select what you want to edit ?\na.Edit Name\nb.Edit Number\n")
        if whatToEdit == "b" :
            number = input("Enter a new contact Number : ")
            while not isValidPhoneNumber(number): 
                print("Enter a valid phone number : ")
                number = input("Enter Contact number : ")
            update(db, "contact", "number", "name" , number ,name)
            print("number updated successfully")
        else:
            new_name = input("Enter a new contact Name : ")
            update(db, "contact", "name", "name" , new_name ,name)
            print("name updated successfully")
    else:
        print("Contact is not saved")
    
    db.commit()
    db.close()