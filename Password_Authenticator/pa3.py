'''
Successor of pa2.py Module
This codebase consist of some more functionalitis like:
- It can matches the Username entered with the password given in db
- It can check db for username and password and authenticate every time untill user give the correct input for UerName ans Password.
- It can limit the number of times user entered the wrong username and password (2 times allowed to enter wrong username or password)
- It can add the entry in db if the username is not there
'''

import getpass

db = {
    "spathak4":"car123",
    "nmodi2002":"repeat2002",
    "ashah":"MotaBhai4UP",
}

uname = input("Enter your UserName : ")

i = 0
while i < 2 and uname not in db.keys():
    uname = input(f"{uname} does not exist in DB!\nRetype UserName : ")
    i += 1

if i == 2 and uname not in db.keys():
    print("Login attempts exceeded. Please try again later.")

else:
    pas = getpass.getpass(f"Welcome {uname}!\nPlease Enter your password : ")

    j = 0
    while j < 2 and pas != db[uname]:
        # print(uname, pas, db[uname])        # This line is just for the debugging purpose - to see the applied combination
        pas = getpass.getpass("Wrong Password! Please retype : ")
        j += 1

    if j == 2 and pas != db[uname]:
        print("Password failed many times. Please try again later.")
    else:
        print("Login Successful...")
