import sqlite3
from prettytable import PrettyTable
from db_helper import select_pattern

def search():
    db = sqlite3.connect("contacts.db")
    t = PrettyTable(['Name', 'Contact Number'])
    what = input("select what to search \na.Name\nb.Number\n")
    if what == "a":
        name = input("Enter a name : ")
        allContacts = select_pattern(db, "contact","name",name)
        
    else:
        number = input("Enter a number : ")
        allContacts = select_pattern(db, "contact","number",number)
    if allContacts:
        for i in allContacts:
            t.add_row([i[0],i[1]])
        print(t)
        t.clear()
    else:
        print("No Contacts found")
    db.close()

