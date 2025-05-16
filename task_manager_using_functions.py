
import datetime

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open("user.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(", ")
                    if username == stored_username and password == stored_password:
                        print("Login successful!")
                        return username  # Return the username upon successful login
                else:  # This else is associated with the for loop
                    print("Invalid username or password. Please try again.")
        except FileNotFoundError:
            print("User file not found. Please contact an administrator.")
            return None  # Return None if the file is not found


def register_user():
    while True:
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
            try:
                with open("user.txt", "a") as file:
                    file.write(f"{new_username}, {new_password}\n")
                print("User registered successfully!")
                return  # Exit registration after successful registration
            except FileNotFoundError:
                print("User file not found. Please contact an administrator.")
                return
        else:
            print("Passwords do not match. Please try again.")

def add_task():
    try:
        with open("tasks.txt", "a") as file:
            assigned_to = input("Enter username of person assigned to the task: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            assigned_date = datetime.date.today().strftime("%Y-%m-%d")  # Get current date
            file.write(f"{assigned_to},{title},{description},{assigned_date},{due_date},No\n")
        print("Task added successfully!")
    except FileNotFoundError:
        print("Tasks file not found. Please contact an administrator.")


def view_all_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                print("\nAssigned to: " + parts[0])
                print("Task: " + parts[1])
                print("Task Description: " + parts[2])
                print("Date Assigned: " + parts[3])
                print("Task Due Date: " + parts[4])
                print("Completed: " + parts[5])
                print("-" * 20)
    except FileNotFoundError:
        print("Tasks file not found. Please contact an administrator.")


def view_my_tasks(current_user):
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                #assigned_to, title, description, assigned_date, due_date, completed = line.strip().split(",")
                assigned_to =  line.strip().split(",")
                if assigned_to == current_user:
                    parts = line.strip().split(", ")
                    print("\nAssigned to: " + parts[0])
                    print("Task: " + parts[1])
                    print("Task Description: " + parts[2])
                    print("Date Assigned: " + parts[3])
                    print("Task Due Date: " + parts[4])
                    print("Completed: " + parts[5])
                    print("-" * 20)
    except FileNotFoundError:
        print("Tasks file not found. Please contact an administrator.")


# Main program loop
current_user = None  # Initialize current_user

while current_user is None:  # Loop until user successfully logs in
    current_user = login()

if current_user:  # Proceed only if login was successful
    while True:
        print("\nMenu:")
        print("r - register a user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

        choice = input("Enter your choice: ")

        if choice == "r":
            register_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            view_my_tasks(current_user)
        elif choice == "e":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
