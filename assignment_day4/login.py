import getpass
credentials = {"bruce":"1234","mary":"457","jonh":"785"}

user_name = input("Enter Username: ")
#password = input("Enter Password: ")
password = getpass.getpass("Enter Password: ")

if user_name in credentials:
    if password == credentials[user_name]:
        print(f"Welcome {user_name}")

    else:
        print(f"Wrong password, try again")

else:
    print("Create Account")