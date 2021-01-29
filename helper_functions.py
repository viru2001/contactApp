import re
import re
from db_helper import select
def isContactSaved(db,name):
    result = select(db, "contact", "*", "name" , name)
    if result:
        return True
    else:
        return False

def isValidPhoneNumber(number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(number)
