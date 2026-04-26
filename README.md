# Python Password Locker

A simple command-line password manager written in Python.
This project allows users to store and retrieve account passwords using a master password for authentication.

The program demonstrates fundamental backend concepts such as password hashing, JSON-based storage, and modular CLI design.

---
## Why I Built This

This project was built as part of my early exploration into Python and backend system design.

Rather than relying on high-level tools, I focused on understanding how core components work under the hood, including:
- File-based data persistence
- Authentication flow using hashing
- Command-line interface structuring
- Input validation and modular design 

The goal was not to build a production-ready password manager, but to understand how such systems are structured at a fundamental level.

---

## Key Learning Outcomes

Through this project, I developed practical understanding of:

- Structuring CLI applications using command-function mapping
- Separating logic into modules (e.g., password validation)
- Handling persistent storage with JSON
- Implementing basic authentication using hashing
- Designing user interaction flows in a terminal environment

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

When the program starts, you will be prompted to enter the master password (A predefined master password - password123, is used for demonstration purposes).

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

1. The user is prompted to enter a master password.
2. The input is hashed using SHA-256 and compared to a stored hash in `master.key`.
3. Upon successful authentication, the application loads stored credentials from `passwords.json`.
4. Commands are mapped to functions using a dictionary-based dispatch system.
5. Passwords can be added, retrieved (copied to clipboard), viewed (masked), or removed.
6. Updates are written back to the JSON file to maintain persistence.

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

This project was built **strictly for learning purposes** and is not intended for real-world use.

While it implements basic authentication using SHA-256 hashing, it does not follow industry-standard security practices.

Key limitations include:

- Passwords are stored in plaintext within `passwords.json`
- No encryption is applied to stored credentials
- No salting or key derivation (e.g., bcrypt, PBKDF2)
- No protection against brute-force attacks

This project helped highlight the difference between *functional systems* and *secure systems*, which is a key consideration in real-world software development.

---

## Future Direction

Future iterations of this project could include:

- Encrypting stored credentials using symmetric encryption
- Implementing secure password hashing (e.g., bcrypt or Argon2)
- Introducing structured error handling
- Improving CLI usability and feedback
- Refactoring into a more scalable architecture

These improvements reflect my ongoing transition from building functional systems to designing more robust and secure applications.

---

## Author

Lotanna Henry

---

## License

This project is open-source and available under the MIT License.
