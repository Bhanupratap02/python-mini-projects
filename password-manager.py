# from cryptography.fernet import Fernet
def view():
    with open("passwords.txt","r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: {user}, Password: {password}")


def add():
    name = input("Enter you username: ")
    password = input("Enter your password: ")
    with open("passwords.txt","a") as file:
        file.write(name + "|" + password + "\n")
while True:
    mode = input("Would You like to add a new password or view exsting ones or type q to quit. (add,view,q): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input")