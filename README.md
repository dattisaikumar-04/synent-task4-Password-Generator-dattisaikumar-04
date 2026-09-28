# 🔐 Password Generator (CLI)

A simple **Command-Line Password Generator** that creates strong random passwords using a combination of uppercase letters, lowercase letters, numbers, and special characters.

## 📌 Objective

Build a CLI-based password generator that creates a strong and random password based on the user's selected password length.

## ✨ Features

* 🔠 Includes uppercase letters
* 🔡 Includes lowercase letters
* 🔢 Includes numbers
* 🔣 Includes special characters
* 🎲 Uses Python's `random` module
* 📏 Allows the user to specify password length
* 🔐 Generates a random password

## 🛠️ Password Components

The generated password can contain:

| Character Type     | Examples    |
| ------------------ | ----------- |
| Uppercase          | `A B C D`   |
| Lowercase          | `a b c d`   |
| Numbers            | `0 1 2 3`   |
| Special Characters | `@ # $ % !` |

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Open the project folder:

```bash
cd password-generator
```

Run the program:

```bash
python password_generator.py
```

## 💡 Example Output

```text
🔐 Password Generator

Enter password length: 12

Generated Password:
G7@kP2!xQ9#m
```

Every time the program runs, it generates a different random password.

## ⚙️ How It Works

1. The user enters the required password length.
2. The program creates a character set containing:

   * Uppercase letters
   * Lowercase letters
   * Numbers
   * Special characters
3. The `random` module selects characters randomly.
4. The selected characters are combined to create the password.
5. The generated password is displayed in the terminal.

## 📚 Concepts Used

* Python `random` module
* User Input
* Strings
* Variables
* Loops
* Lists/Character Sets
* Random Selection
* Basic CLI Programming

## 🎯 Learning Outcome

By completing this project, you will understand how to work with Python's randomization features and character sets to generate random passwords through a command-line application.



