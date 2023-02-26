import getpass

db = {
    "spathak4":"car123",
    "nmodi2002":"repeat2002",
    "ashah":"MotaBhai4UP",
}

uname = input("Enter your UserName : ")
pas = getpass.getpass(f"Welcome {uname}!\nPlease Enter your password : ")

for i in db.keys():
    if uname == i:
        while pas != db.get(i):
            pas = getpass.getpass("Wrong Password! Please retype : ")

print("Login Successful...")