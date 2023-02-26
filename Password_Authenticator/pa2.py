'''
Successor of pa.py Module
This codebase consist of some more functionalitis like:
- It can matches the Username entered with the password given in db
- It can check db for username and password and authenticate every time untill user give the correct input for UerName ans Password.
'''

import getpass

db = {
    "spathak4":"car123",
    "nmodi2002":"repeat2002",
    "ashah":"MotaBhai4UP",
}

uname = input("Enter your UserName : ")

while uname not in db.keys():
    uname = input(f"{uname} does not exist in DB!\nRetype UserName : ")

pas = getpass.getpass(f"Welcome {uname}!\nPlease Enter your password : ")

while pas != db[uname]:
    # print(uname, pas, db[uname])        # This line is just for the debugging purpose - to see the applied combination
    pas = getpass.getpass("Wrong Password! Please retype : ")

print("Login Successful...")
