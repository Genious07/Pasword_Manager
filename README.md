Password Manager in Python
Overview
This project is a command-line password manager written in Python that allows users to securely store and manage their account passwords. It supports multiple users, each with their own login credentials, and saves passwords in an encrypted form within a single CSV file.

Key Features:
User Authentication: Users can create accounts with a username and password. The login password is hashed using bcrypt for secure storage.
Password Encryption: Account passwords are encrypted using the Fernet encryption from the cryptography library.
Add, View, Edit Passwords: Users can add, view, and edit passwords for their accounts.
Change Login Password: Users can change their login password.
All Data Stored in a Single CSV File: User login credentials and encrypted passwords are stored together in a single CSV file.
Requirements
The following Python libraries are required for the project:

bcrypt: For secure hashing of user passwords.
cryptography: For encryption and decryption of account passwords.
csv: For reading and writing user data in CSV format.
os: For handling file operations.
You can install these dependencies using pip:

bash
Copy code
pip install bcrypt cryptography
Usage
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/password-manager.git
cd password-manager
2. Run the script
Run the Python script password_manager.py to start the program.

bash
Copy code
python password_manager.py
3. Creating a New User
When you run the program for the first time and input a username that does not exist, it will prompt you to create a new user by setting a password.
Your login password will be hashed and stored securely in the user_data.csv file.
4. Logging In
After the user is created, you can log in by entering your username and password. The program will verify the entered password with the stored hashed password.
5. Managing Passwords
After logging in, you can perform the following tasks:

Add Password: Add a new account password (account name, account username, and account password).
View Passwords: View stored account passwords (passwords will be decrypted before displaying).
Edit Password: Edit an existing account password.
Change Login Password: Update the login password for your account.
6. Exit
You can exit the program by selecting the Exit option from the task menu.

CSV File Structure
All user and password data is stored in a single CSV file named user_data.csv. The file has the following structure:

Copy code
username, hashed_password, account_name, account_username, encrypted_account_password
For each user, the username and hashed_password are stored along with the encrypted account details.

Encryption Details
Encryption Algorithm: Fernet encryption from the cryptography library is used to secure account passwords.
Key Storage: A unique encryption key is generated and stored in a key.key file upon the first run of the program. This key is required to encrypt and decrypt account passwords.
Example
Adding a Password
markdown
Copy code
-------Password Manager--------
Enter username: user1
Enter password: ******
Welcome, user1!

What task do you want to perform?
1. Add password
2. View passwords
3. Edit password
4. Change login password
5. Exit
Choose an option (1-5): 1

Enter account name: GitHub
Enter account username: user1
Enter account password: mypassword123

Password saved successfully!
Viewing Passwords
yaml
Copy code
Stored passwords:
Account: GitHub, Username: user1, Password: mypassword123
Security Considerations
Password Hashing: User login passwords are hashed using bcrypt, providing strong resistance against brute force attacks.
Password Encryption: Account passwords are encrypted using a symmetric key encryption (Fernet), making it hard to recover them without access to the encryption key.
CSV Storage: All data is stored in a CSV file. It is recommended to keep this file secure and avoid exposing it to unauthorized access.
Future Improvements
Add support for GUI (Graphical User Interface) to enhance user experience.
Implement password strength validation to enforce stronger user passwords.
Add features such as password expiration alerts and password generation tools.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this code as long as the original author is credited.

Author
Developed by Satwik Singh
