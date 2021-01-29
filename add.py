import sqlite3
from db_helper import insert


def add(name,number):
    db = sqlite3.connect("contacts.db")
    insert(db, "contact" , name,number)
    db.commit()
    db.close()
    