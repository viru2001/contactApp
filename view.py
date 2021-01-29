import sqlite3
from prettytable import PrettyTable
from db_helper import select_all

def view():
    db = sqlite3.connect("contacts.db")
    t = PrettyTable(['Name', 'Contact Number'])
    allContacts = select_all(db, "contact")
    for i in allContacts:
        t.add_row([i[0],i[1]])
    print(t)
    t.clear()
    db.close()
