import sys
import json
import hashlib
import pwinput
import pyperclip

"""
    An insecure password locker program
    with python
"""

def load_passwords():
    with open("passwords.json", "r") as file:
        return json.load(file)

def update_passwords(new_passwords):
    with open("passwords.json", "w") as file:
        json.dump(new_passwords, file)

def find():
    print("Enter account you would like to find:")
    account = input()
    try:
        password = passwords[account]
        pyperclip.copy(password)
        print("Password copied to clipboard successfully!")
    except KeyError:
        print("Account name not found!")


def view():
    print("Accounts".ljust(15, " "), end="")
    print("Passwords".rjust(15, " "))
    print("_"*30)
    for k, v in passwords.items():
        print(k.ljust(15, "-"), end="")
        print("--[*ENCRYPTED*]".rjust(15, " "))


def add():
    print("Enter new account name: ")
    new_acc = input()
    if not new_acc:
        print("Account name cannot be empty!")
        return
    print("Enter new password: ")
    new_password = pwinput.pwinput(prompt="", mask="*")
    if not new_password:
        print("Password cannot be empty!")
        return
    if new_acc not in passwords:
        passwords[new_acc] = new_password
        update_passwords(passwords)
        print("Password database successfully updated!")
    else:
        print("Account already exists!")
        print("Would you like to update it? (y/n)")
        ans = input()
        if ans == 'y':
            passwords[new_acc] = new_password
            update_passwords(passwords)
            print("Password database successfully updated!")
        elif ans == 'n':
            return
        else:
            print("Invalid response")

def remove():
    print("Enter account you would like to remove:")
    account = input()
    if not account:
        print("Account entry cannot be empty!")
        return
    if account in passwords:
        del passwords[account]
        update_passwords(passwords)
        print("Password database successfully updated!")
    else:
        print("Account not found!")

def get_help():
    print('''
        find - Find an account's password
        view - View all account passwords
        add - Add a new account's password
        remove - Remove a current account from database
        help - shows this help menu
    ''')

if __name__ == '__main__':
    commands = {
        'find': find,
        'view': view,
        'add': add,
        'remove': remove,
        'help': get_help
    }

    print("Welcome to Password Locker, Mr Henry!")

    def verify_master_key():
        with open("master.key", "r") as f:
            correct_hash = f.read().strip()

        print("Please confirm it's you: (Enter password)")
        inputed_password = pwinput.pwinput(prompt="", mask="*")
        hashed_input = hashlib.sha256(inputed_password.encode()).hexdigest()
        if correct_hash == hashed_input:
            print("Welcome Sir...")
            return True
        else:
            return False

    if verify_master_key():
        passwords = load_passwords()
        while True:
            print("Enter command you would wish to execute: find, view, add, remove, help, quit")
            command = input().lower().strip()
            if command in commands:
                func = commands[command]
                func()
            elif command == 'quit':
                sys.exit()
            else:
                print("Invalid command!")
    else:
        print("INTRUDER ALERT!!! SHUTDOWN PROTOCOL INITIATED!!!")
        sys.exit()
