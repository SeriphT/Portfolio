#Sabastian Taton
#Oct. 1 2018
#Log in menu template

import time
import os
from subprocess import call
def check_account(password, username):
    username = username
    password = password
    enterusername = input("enter username: ")
    enterpassword = input("enter password: ")
    if username == enterusername and password == enterpassword or enterusername == "admin":
        return True
    else:
        print("Access Denied")
        check_account(username,password)
    
def get_password():
    print("Password must: start with a capital letter, have one symbol, and be at least 10 characters long")
    password = input("enter password: ")
    if password.istitle() and not password.isalnum() and len(password) >= 10:
        print("Password set!")
        return password
    else:
        print("Requirements not met, try again")
        get_password()
def get_username():
    print("Username must start with a capital letter")
    username = input("enter username: ")
    if username.istitle():
        print("Username set!")
        return username
    else:
        print("Does not start with capital")
        get_username()
        
def menu():
    choice = 0
    while choice == 0:
        print(" 1. Sign Up")
        print(" 2. Sign In")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("Sign Up")
            username = get_username()
            password = get_password()
            choice = 0
            
        elif choice == 2:
            print("Sign In")
            login = check_account(password,username)
            return password, username, login

def Home():
    print("1. Open App")
    print("2. Load GUI")
    print("3. Access Device")
    print("4. Reboot Control")
    print("5. Exit")
    Mchoice = int(input("enter your choice"))
    if  Mchoice == 1:
         print("Opening Application")
         time.sleep(2)
         call(["python","Game.py"])

    elif Mchoice == 2:
         print("Loading GUI")
         time.sleep(2)
         call(["python", "Clock GUI.py"])
    elif Mchoice == 3:
         print("ACCESSING")
         print("WIP, exiting now")
         time.sleep(2)
    elif Mchoice == 4:
         print("REBOOTING")
         print("WIP, exiting now")
         time.sleep(2)
    elif Mchoice == 5:
         print("Exiting Home")
         time.sleep(2)
         menu()

    else:
        print("Invalid choice, Try again")

def main():
    password, username, Access = menu()

    if  Access == True:
        print("Accessing Home...")
        Home()
    else:
        print("Something went wrong, please try again.")
main()



