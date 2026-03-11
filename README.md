# Python Password Locker

A simple command-line password manager written in Python.
This project allows users to store and retrieve account passwords using a master password for authentication.

The program demonstrates fundamental backend concepts such as password hashing, JSON-based storage, and modular CLI design.

---

## Features

* Master password authentication using SHA-256 hashing
* Masked password input
* Copy stored passwords directly to the clipboard
* Persistent password storage using JSON
* Command-line interface
* Add, remove, view, and retrieve account passwords
* Help menu for available commands

---

## Technologies Used

* Python 3
* `pyperclip` for clipboard interaction
* `pwinput` for masked password input
* `hashlib` for password hashing
* `json` for data storage

---

## Installation

Clone the repository:

```bash
git clone https://github.com/loteehenry/python-password-locker.git
cd python-password-locker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run the script using:

```bash
python password_locker.py
```

When the program starts, you will be prompted to enter the master password (which is password123).

---

## Usage

Available commands:

| Command  | Description                                     |
| -------- | ----------------------------------------------- |
| `find`   | Copy a stored account password to the clipboard |
| `view`   | View stored account names                       |
| `add`    | Add a new account and password                  |
| `remove` | Delete an account from the database             |
| `help`   | Show available commands                         |
| `quit`   | Exit the program                                |

Example session:

```
Enter command you would wish to execute: find, view, add, remove, help, quit
add
Enter new account name:
github
Enter new password:
********
Password database successfully updated!
```

---

## How It Works

1. The user authenticates with a master password.
2. The master password is hashed using SHA-256 and compared to the stored hash in `master.key`.
3. Account passwords are stored in `passwords.json`.
4. When a user retrieves a password, it is copied directly to the system clipboard.

---

## Project Structure

```
python-password-locker/
│
├── password_locker.py
├── passwords.json
├── master.key
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Security Notice

This project was built for **learning purposes** and should not be used as a production password manager.

Limitations include:

* Account passwords are stored in plaintext in `passwords.json`
* No encryption of stored credentials
* No salting or key-derivation for the master password
* No protection against brute-force attacks

Real-world password managers use encryption and specialized libraries to protect stored credentials.

---

## Future Improvements

Possible improvements for this project:

* Encrypt stored passwords
* Implement salted password hashing
* Add account search functionality
* Improve command-line interface
* Add logging and error handling

---

## Author

Lotanna Henry

---

## License

This project is open-source and available under the MIT License.
