import getpass

def read_passwd_file(file_path):
    """
    Reads user data from the password file.

    Args:
    - file_path (str): Path to the password file.

    Returns:
    - dict: A dictionary containing user information with usernames as keys and tuples (real_name, password) as values.
    """
    users = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                username, real_name, password = line.strip().split(':')
                users[username] = (real_name, password)
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist
    return users

def write_passwd_file(file_path, users):
    """
    Writes user data to the password file.

    Args:
    - file_path (str): Path to the password file.
    - users (dict): A dictionary containing user information.
    """
    with open(file_path, 'w') as file:
        for username, (real_name, password) in users.items():
            file.write(f"{username}:{real_name}:{password}\n")

def validate_password(username, password, users):
    """
    Validates the provided password.

    Args:
    - username (str): Username to validate.
    - password (str): Password to validate.
    - users (dict): A dictionary containing user information.

    Returns:
    - bool: True if the password is valid for the given username, False otherwise.
    """
    return users.get(username, ('', ''))[1] == password

def add_user(file_path):
    """
    Adds a new user to the password file.

    Args:
    - file_path (str): Path to the password file.
    """
    users = read_passwd_file(file_path)

    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    if username not in users:
        users[username] = (real_name, password)
        write_passwd_file(file_path, users)
        print("User Created.")
    else:
        print("Cannot add. Username already exists.")

def delete_user(file_path):
    """
    Deletes a user from the password file.

    Args:
    - file_path (str): Path to the password file.
    """
    users = read_passwd_file(file_path)

    username = input("Enter username: ")

    if username in users:
        del users[username]
        write_passwd_file(file_path, users)
        print("User Deleted")
    else:
        print("User not found")

def change_password(file_path):
    """
    Changes the password of an existing user.

    Args:
    - file_path (str): Path to the password file.
    """
    users = read_passwd_file(file_path)

    username = input("User: ")

    if username in users:
        current_password = getpass.getpass("Current Password: ")
        if validate_password(username, current_password, users):
            new_password = getpass.getpass("New Password: ")
            confirm_password = getpass.getpass("Confirm: ")

            if new_password == confirm_password:
                users[username] = (users[username][0], new_password)
                write_passwd_file(file_path, users)
                print("Password changed")
            else:
                print("Passwords do not match")
        else:
            print("Invalid current password")
    else:
        print("User not found")

def login(file_path):
    """
    Logs in a user.

    Args:
    - file_path (str): Path to the password file.
    """
    users = read_passwd_file(file_path)

    username = input("User: ")
    password = getpass.getpass("Password: ")

    if validate_password(username, password, users):
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    file_path = r"C:\Users\dell\OneDrive\Desktop\FOCP_FINAL\Task3\passwd.txt"
    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user(file_path)
        elif choice == "2":
            delete_user(file_path)
        elif choice == "3":
            change_password(file_path)
        elif choice == "4":
            login(file_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

            