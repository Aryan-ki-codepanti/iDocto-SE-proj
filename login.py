from os.path import exists
from getpass import getpass
import pickle


def login():
    users_file = "user.dat"
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    roles = ["doctor", "patient", "clinic"]

    print("ROLES")
    print("1. Doctor")
    print("2. Patient")
    print("3. Clinic")
    c = input("Select a role : ")

    if c not in ('1','2','3'):
        print("Invalid Selection")
        return

    role = roles[int(c) - 1]

    if not exists(users_file):
        with open(users_file, "wb") as f:
            pickle.dump({
                "patient": [],
                "doctor": [],
                "clinic": []
            }, f)

    with open(users_file, "rb") as f2:
        data = pickle.load(f2)[role]

        found = False
        for user in data:
            if user.username == username:
                found = True
                break

        if not found:
            print(f"User not found for role : {role}")

        elif user.password != password:
            print(f"Incorrect password")
        
        else: 
            print(f"Successfully logged in as @{username}")

login()
