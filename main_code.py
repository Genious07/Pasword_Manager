import bcrypt
import csv
from cryptography.fernet import Fernet
import os


# Generate or load the encryption key
def load_or_generate_key():
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        return key


# Encrypt a password using Fernet
def encrypt_password(password, fernet):
    return fernet.encrypt(password.encode()).decode()


# Decrypt a password using Fernet
def decrypt_password(encrypted_password, fernet):
    return fernet.decrypt(encrypted_password.encode()).decode()


# Hash a password for user login
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


# Verify the entered password against the stored hash
def verify_password(stored_hash, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_hash)


# Function to load all user data from a CSV file
def load_users_and_passwords(csv_file='user_data.csv'):
    users = {}
    if os.path.exists(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                username, hashed_password, account, acc_username, encrypted_password = row
                if username not in users:
                    users[username] = {
                        'password': hashed_password,
                        'accounts': []
                    }
                users[username]['accounts'].append([account, acc_username, encrypted_password])
    return users


# Function to save the new user's password and data to the CSV file
def save_user_data(username, hashed_password, account, acc_username, password, fernet, csv_file='user_data.csv'):
    encrypted_password = encrypt_password(password, fernet)
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password, account, acc_username, encrypted_password])


# Display stored passwords for a user (decrypt them before showing)
def display_passwords(user_data, fernet):
    for account, acc_username, encrypted_password in user_data:
        decrypted_password = decrypt_password(encrypted_password, fernet)
        print(f"Account: {account}, Username: {acc_username}, Password: {decrypted_password}")


# Edit an existing password for a user
def edit_password(users, username, fernet, account_name):
    for i, (account, acc_username, encrypted_password) in enumerate(users[username]['accounts']):
        if account == account_name:
            new_password = input(f"Enter new password for {account}: ")
            users[username]['accounts'][i][2] = encrypt_password(new_password, fernet)
            save_all_users(users)  # Overwrite the file
            print(f"Password updated for {account_name}")
            return
    print(f"No account found with name {account_name}")


# Function to overwrite the entire user data file after changes
def save_all_users(users, csv_file='user_data.csv'):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for username, data in users.items():
            for account in data['accounts']:
                writer.writerow([username, data['password'], *account])


# Change the login password for a user
def change_login_password(users, username):
    new_password = input("Enter new password: ")
    hashed_password = hash_password(new_password)
    users[username]['password'] = hashed_password.decode()
    save_all_users(users)
    print("Login password changed successfully!")


# Main logic for the password manager
def main():
    fernet = Fernet(load_or_generate_key())

    # Load all users and passwords from the CSV file
    users = load_users_and_passwords()

    # Login page
    print("-------Password Manager--------")
    username = input("Enter username: ")

    # Check if the user already exists
    if username in users:
        # Verify the user's password
        password = input("Enter password: ")
        stored_hash = users[username]['password'].encode()
        if not verify_password(stored_hash, password):
            print("Incorrect username or password!")
            return
    else:
        # New user - set up username and password
        print("Creating new user...")
        password = input("Set a new password: ")
        hashed_password = hash_password(password).decode()
        users[username] = {'password': hashed_password, 'accounts': []}
        print("User created successfully!")

    # Welcome message
    print(f"Welcome, {username.upper()}!")

    # Task selection menu
    while True:
        print("\nWhat task do you want to perform?")
        print("1. Add password")
        print("2. View passwords")
        print("3. Edit password")
        print("4. Change login password")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            # Add password
            account = input("Enter account name: ")
            acc_username = input("Enter account username: ")
            acc_password = input("Enter account password: ")
            save_user_data(username, users[username]['password'], account, acc_username, acc_password, fernet)
            users = load_users_and_passwords()  # Reload users to reflect new entries
            print("Password saved successfully!")

        elif choice == '2':
            # View passwords
            print("Stored passwords:")
            display_passwords(users[username]['accounts'], fernet)

        elif choice == '3':
            # Edit password
            account_name = input("Enter the account name to edit the password: ")
            edit_password(users, username, fernet, account_name)

        elif choice == '4':
            # Change login password
            change_login_password(users, username)

        elif choice == '5':
            print("Exiting password manager. Goodbye!")
            break

        else:
            print("Invalid option, please choose again.")


if __name__ == "__main__":
    main()
