# user_manager.py

FILE_NAME = "file.txt"

def add_user():
    # Take input from user
    user = input("Enter username: ")

    # Save user to file (append mode)
    with open(FILE_NAME, "a") as f:
        f.write(user + "\n")

    print(f"User '{user}' added successfully.")

def show_users():
    try:
        with open(FILE_NAME, "r") as f:
            users = f.readlines()

        users = [u.strip() for u in users if u.strip()]

        if users:
            print("\nAll Users (previous + current):")
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user}")
        else:
            print("No users found.")
    except FileNotFoundError:
        print("No users found (file does not exist yet).")

if __name__ == "__main__":
    add_user()
    show_users()
