import sqlite3
from db_helper import delete
from helper_functions import isContactSaved

def deletee(name):
    db = sqlite3.connect("contacts.db")
    if isContactSaved(db,name):
        delete(db,"contact","name",name)
        print("contact deleted successfully")
    else:
        print("Contact is not saved")
    db.commit()
    db.close()