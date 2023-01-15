import os
import numpy as np
import json

while True:
    operation = input("Please input operation:\n1) register\n2) log in\n:")
    if operation == "1":
        username = input("Username: ")
        unsize = len(username)

        if unsize < 4:
            while True:
                username = input("length of your username is less then 4, reinput please: ")
                unsize = len(username)
                if unsize < 4:
                    continue
                elif unsize >= 4:
                    break
        
        password = input("Password: ")
        pslen = len(password)
        if pslen < 6:
            while True:
                password = input("length of your password is less then 6, reinput please: ")
                pslen = len(password)
                if pslen < 6:
                    continue
                elif pslen >= 6:
                    break

        fileloc = "information.json"
        with open(fileloc, "w") as file_object:
            account_info = {
                "username": username,
                "password": password
            }
            json.dump(account_info, file_object)
            print("Account registered successfully.")
            break
    elif operation == "2":
        username = input("Username: ")
        password = input("Password: ")
        
        fileloc = "information.json"
        with open(fileloc, "r") as file_object:
            account_info = json.load(file_object)
            if account_info["username"] == username and account_info["password"] == password:
                print("Login successful.")
                break
            else:
                print("Incorrect username or password. Please try again.")
