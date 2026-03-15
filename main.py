import random
import string

# Dictionary to store passwords
passwords = {}

# Function to generate strong password
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to save password
def save_password():
    account = input("Enter account name: ")
    password = input("Enter password: ")
    passwords[account] = password
    print("Password saved successfully!")

# Function to retrieve password
def get_password():
    account = input("Enter account name: ")
    if account in passwords:
        print("Password:", passwords[account])
    else:
        print("Account not found!")

# Main program
while True:
    print("\nPassword Manager")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Retrieve Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Generated Password:", generate_password())
    elif choice == "2":
        save_password()
    elif choice == "3":
        get_password()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")