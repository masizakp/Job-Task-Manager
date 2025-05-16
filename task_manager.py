
import datetime

stored_username = []
stored_password = []

# This is a user login space. The username and password will be requested
# from the user input and user.txt file will be read and test if the user
# exists in the file and the message "Login successful!" will be displayed,
# but if the username and password do not match the one in the file, the
# message "Invalid username or password." will be displayed
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("user.txt", "r", encoding='utf-8') as file:
            for line in file:
                temp = line.strip().split(", ")
                stored_username.append(temp[0])
                stored_password.append(temp[1])
            
            for i in range(len(stored_username)):
                if username == stored_username[i
                ] and password == stored_password[i]:
                    print("Login successful!")
                    break
            else:
                print("Invalid username or password.")
                continue
        break
    except FileNotFoundError:
        print("user.txt file not found.")
        break
    
# The menu will always appear for user to choose from but only the
# admin will be having a menu with "st - view task/ user statistics" option
while True:
    if username == stored_username[0]:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    st - view task/ user statistics
    e - exit
    : ''').lower()
    else:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks  
    e - exit
    : ''').lower()

    # If the user's choice is "r", new user will be added.
    # The user username, password and password confirmation will be needed
    # The user.txt file will be opened and new user with the entered
    # credentials will be appended as a line in the user.txt file.
    # The message "User added" will be displayed if the user doesn't
    # exist already in the file but the message "User already exist" will be
    # displayed if the username is already in the file
    if menu == "r":
        if username == stored_username[0]:
            new_username = input("Enter new username: ")
            while True:
                if new_username in stored_username:
                    print("Username already exist!")
                    break
                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")
                if new_password != confirm_password:
                    print("Password mismatch!")
                    continue
                else:
                    try:
                        with open("user.txt", "a", encoding='utf-8') as file:
                            file.write(f"\n{new_username}, {new_password}")
                        print("User registered successfully.")
                        break                            
                    except FileNotFoundError:
                        print("user.txt file not found.")
                        exit()
        else:
            print("Only admin is permitted to register a user!")
        
    # If the user's choice is "a", the tasks.txt will be opened and user input
    # will be appended and stored in the tasks file as lines, each user input
    # will be separated by comma
    # The message "Task added successfully!" will be displayed
    elif menu == 'a':
        with open("tasks.txt", "a", encoding='utf-8') as file:
            try:
                add_username = input(
                "Enter the name of the personnel assigned to: "
                )
                add_title = input("Enter the title of the task: ")
                add_description = input(
                "Enter the task description: "
                )
                add_task_due_date = input(
                "Enter the date that the task is due (DD MM YYYY): "
                )
                add_assigned_date = datetime.datetime.today(
                ).strftime("%d %b %Y")
                add_task_complete = "No"
                
                file.write(", ".join([
                    add_username, add_title, add_description,
                    add_task_due_date, add_assigned_date,
                    add_task_complete]) + "\n"
                    )
                print("Task added successfully!")
            except FileNotFoundError:
                print("user.txt file not found.")

    # If the user's choice is "va", the tasks.txt will be opened and read as
    # lines. Only admin is allowed to view all the tasks in the file in a
    # formatted way. The message "Only Admin is allowed to view all the
    # tasks!" will be displayed if any user but admin is trying to view all
    # the files
    elif menu == 'va':
        try:
            with open("user.txt", "r", encoding='utf-8') as user_file:
                #if username == stored_username[0]:
                with open(
                    "tasks.txt", "r", encoding='utf-8') as tasks_file:
                    lines = tasks_file.readlines()
                    for line in lines:
                        parts = line.strip().split(",")
                        if len(parts) == 6:
                            print(
                                "\nAssigned to: ", parts[0],
                                "\nTask: ", parts[1],
                                "\nTask Description: ", parts[2], 
                                "\nDate Assigned: ", parts[3], 
                                "\nTask Due Date: ", parts[4], 
                                "\nCompleted: ", parts[5]
                                )
                            print("=" * 50)
                        else:
                            print(
                                f"Warning: Incorrect format"
                                f"in line: {line.strip()}"
                                )                
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # If the user's choice is "vm", the tasks.txt will be opened and read
    # as lines. All the users can view their respective tasks and the tasks
    # in the file will appear in a formatted way
    elif menu == 'vm':
        with open("tasks.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        try:
            for line in lines:
                parts = line.strip().split(", ")
                if parts[0] == username:
                    print("\nAssigned to: ", parts[0],
                        "\nTask: ", parts[1],
                        "\nTask Description: ", parts[2],
                        "\nDate Assigned: ", parts[3], 
                        "\nTask Due Date: ", parts[4], 
                        "\nCompleted: ", parts[5]
                        )
                    print("="* 50)
        except FileNotFoundError:
            print("user.txt file not found.")

    # If the user's input choice is "st" the file user.txt / task.txt will
    # be opened and number of lines in the file will be read and stored in
    # the variable called task_counter and user_counter.
    # The number of users and tasks will be displayed
    elif menu == "st":
        try:
            if username == stored_username[0]:
                with open("tasks.txt", "r", encoding='utf-8') as file:
                    task_counter = len(file.readlines())
                    print(f"There are {task_counter} tasks in the file.")
                
                with open("user.txt", "r", encoding='utf-8') as file:
                    user_counter = len(file.readlines())
                    print(f"There are {user_counter} users in the file.")
                print("="*50)
            else:
                print("Only admin can view the stats")
        except FileNotFoundError:
            print("user.txt file not found.")

    # If the user's input choice is "e" from the menu, the message
    # goodbye will be printed and the function exit will be called
    # and the program will stop
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If the user did not input a specific input from the menu, the
    # message will be displayed
    else:
        print("You have entered an invalid input. Please try again")
