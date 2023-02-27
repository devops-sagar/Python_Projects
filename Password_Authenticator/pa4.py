'''
Successor of pa3.py Module
This codebase consist of some more functionalitis like:
- It can matches the Username entered with the password given in db
- It can check db for username and password and authenticate every time untill user give the correct input for UerName ans Password.
- It can limit the number of times user entered the wrong username and password (2 times allowed to enter wrong username or password)
- It can add the entry in db if the username is not there
- It can ask for resetting the password if user forgot.
'''

import getpass

db = {
    "spathak4":"car123",
    "nmodi2002":"repeat2002",
    "ashah":"MotaBhai4UP",
    "test":"123",
}

uname = input("Enter your UserName : ")

i = 0
while i < 2 and uname not in db.keys():
    uname = input(f"{uname} does not exist in DB!\nRetype UserName : ")
    i += 1

if i == 2 and uname not in db.keys():
    print("Login attempts exceeded. Please try again later.")
    ask_entry = input("Sign Up? [y/n] : ")
    if ask_entry == 'y':
        ask_uname = input("Enter the Username you want : ")
        ask_pas = input("Enter the Password you like : ")
        db[f"{ask_uname}"] = f"{ask_pas}"
        print("Sign Up Successfull...")
        print("Login Successful...")
        # print(db)       #for debugging purpose - to see the updated db
    else:
        print("Bye bye")

else:
    pas = getpass.getpass(f"Welcome {uname}!\nPlease Enter your password : ")

    j = 0
    while j < 2 and pas != db[uname]:
        # print(uname, pas, db[uname])        # This line is just for the debugging purpose - to see the applied combination
        pas = getpass.getpass("Wrong Password! Please retype : ")
        j += 1

    if j == 2 and pas != db[uname]:
        print("Password failed many times. Please try again later.")
        ask_reset_pass = input("Do you want to reset your Password? [y/n] : ")
        if ask_reset_pass == 'y':
            new_pas = input("Enter the new Password you want to set : ")
            db[uname] = f"{new_pas}"
            # print(db)            #for debugging purpose - to see the updated db
    else:
        print("Login Successful...")