from helper_functions import isValidPhoneNumber
import sqlite3

from db_helper import create_table
from add import add
from view import view
from edit import edit
from deletee import deletee
from search import search

db = sqlite3.connect("contacts.db")
create_table(db, 'contact', name='text', number='text')

def runApp():
    while True:
        print("what you want to do ?\n1.Add Contact\n2.View all Contacts\n3.Edit Contact\n4.Delete Contact\n5.Search Contact\n6.Exit")
        choice = int(input())
        if choice == 1:
            name = input("Enter a name : ")
            number = input("Enter Contact number : ") 
            while not isValidPhoneNumber(number): 
                print("Enter a valid phone number")
                number = input("Enter Contact number : ")
            add(name,number)
            print("contact added successfully")
        elif choice == 2:
            view()
        elif choice == 3:
            name = input("Enter a name : ")
            edit(name)
        elif choice == 4:
            name = input("Enter a name : ")
            deletee(name)
        elif choice == 5:
            search()
        elif choice == 6:
            break
        print("\n")
runApp()