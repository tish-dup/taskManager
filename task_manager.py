# Import date from datetime module to be used when assigning a task to an user
from datetime import date

# Import module to search for file in a directory
from os import path


# This function checks whether the username and password is valid when the user signs in.
def sign_in(name, password):
    # Open the file 'user.txt' and read the text
    # Split each line after the line break and assign to an array.
    # This will enable the code to read the file line by line.
    in_file_user = open("user.txt", "r")
    text_line_arr = in_file_user.read().replace(",", "").splitlines()

    # Create False booleans for username and password found to be used in if-statement
    username_found = False
    password_match = False

    # Loop through each line in the text and extract the username and password. Assign it to variables.
    for line in text_line_arr:
        if username_found:
            break
        credentials = line.split()
        user_name = credentials[0]
        user_password = credentials[1]

        # state that if the username and password in the file matches the username and password in the parameter of the
        # function, then they has been found
        if user_name == name:
            username_found = True
            if password == user_password:
                password_match = True

    # If the username and password does not match the username and password in the parameter, then a error message
    # should display.
    if username_found and not password_match:
        print("Either your username or password is not valid. Please enter your username and password: ")
    elif not username_found:
        print("The username and password you provided is not valid. Please enter your username and password: ")

    return username_found and password_match


# This function provides the user with a menu from which they can make a selection.
def get_selection(username):
    # Print out the options for the user
    print("\nPlease select one of the following options:")
    print("r \t - \t register user")
    print("a \t - \t add task")
    print("va \t - \t view all tasks")
    print("vm \t - \t view my tasks")
    if username == "admin":
        print("gr \t - \t generate reports")
        print("ds \t - \t display statistics")
    print("e \t - \t exit")
    # Request user to make their selection
    selection = input("Your selection: ")
    return selection


# This function determines which option should open up based on the selection the user made.
def perform_action(selection, username):
    if selection == "r":
        # Only the user with admin rights is allowed to assign tasks to other users.
        if username != "admin":
            print("You are not authorised to register an user")
            return selection
        else:
            reg_user()
    if selection == "a":
        add_task()
    if selection == "va":
        view_all()
    if selection == "vm":
        view_mine(username)
    if selection == "gr":
        generate_report()
    if selection == "ds":
        display_stats()
    if selection == "e":
        exit(0)


# With this function the user can register another user.
def reg_user():
    # When the admin user selects 'r', they will be prompted to follow the instructions that are necessary
    # to register an user
    new_user = input("Enter new user name: ")
    # The 'user.tct' file is open and read, to determine if the username that was enter already exists.
    read_file_user = open("user.txt", "r")
    user_list = read_file_user.read().split("\n")
    for line_details in user_list:
        details_arr = line_details.split(",")
        line_user = details_arr[0]
        if line_user == new_user:
            print("This user already exists")
            return reg_user()

    # If the username has not been found, the user can continue to register the password.
    new_password = input("Enter user password: ")
    confirm_password = input("Please confirm password: ")

    # The program needs to ensure that the pass word the user entered is correct, by confirming the password.
    # If the confirmation password does not match the original password, the program will prompt the user
    # to enter the password again.
    while new_password != confirm_password:
        print("Your password does not match. Please try again.")
        new_password = input("Enter user password: ")
        confirm_password = input("Please confirm password: ")

    print("User has successfully been registered")

    # The new username and password is now ready to be written to the 'user.txt' file
    out_file_user = open("user.txt", "a")
    out_file_user.seek(0, 2)
    out_file_user.write(new_user + ", " + new_password + "\n")
    out_file_user.close()


# This function enables the user to add a task.
def add_task():

    # Prompt the user to follow the instructions in order to add a new task and assign it to an user.
    print("Please complete the following to add a new task for an user")
    task_assigned_to = input("Enter username: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Description of the task: ")
    task_current_date = date.today()
    date_string = task_current_date.strftime("%d %b %Y")
    task_due_date = input("Enter the due date of the task (day / month / year): ")
    completion = "No"

    # Open the file to which the task should be added and write the task to this file.
    out_file_task = open("tasks.txt", "a")
    out_file_task.write(
        f"{task_assigned_to}, {task_title}, {task_description}, {date_string}, {task_due_date}, {completion}\n")
    out_file_task.close()


# This function allows the user to view all the tasks that has been assigned to all the users.
def view_all():
    # The user can view only the tasks assigned to them by selecting 'va'.
    # To view all the tasks in 'tasks.txt' file.
    # Open the file in readable format
    in_file_task = open("tasks.txt", "r")
    # Read content of file, and assign it to a variable
    text = in_file_task.read()
    # Close the file after use
    in_file_task.close()
    # To display content of file in readable format, replace ','with line breaks.
    text = text.replace(", ", "\n")
    print(text)


# This function allows only shows the tasks of the user who signed in.
def view_mine(username):
    # The user can view only the tasks assigned to them by selecting 'vm'.
    # The program will open the 'task.txt' file in a readable format.
    in_file_task = open("tasks.txt", "r")
    text = in_file_task.read()
    in_file_task.close()
    task_array = text.split("\n")

    # In a for loop, the function runs trough each line in the file and assign it to a variable task. Now we can select
    # the first word of the task which is the username and match it to the user who signed in. This loop also find the
    # index of the task and assigns it to the task. This enables the user to select the task and modify it in a
    # different function.
    # The result are printed out and displayed on the screen.
    for task_line in task_array:
        task = task_line.split(",")

        if task[0] == username:
            index = task_array.index(task_line) + 1
            user_task = task_line.replace(", ", "\n")
            print(f"{index} - {user_task}")

    # The user's selection is assigned to a variable. If the user selects '-1' then they can return to the main
    # function, else a new function is called where they can edit the task they selected.
    task_selection = int(input("\nPlease select the task you wish to modify. To return to the main menu, enter '-1': "))
    if task_selection == -1:
        return
    else:
        edit_task(task_selection, username)


# To edit tasks, this function requires the index of the task and the username.
def edit_task(task_num, name):
    # Print the edit options for the user and assign user's selection to a variable.
    print("1\t-\tMark the task as complete\n2\t-\tEdit the task")
    user_option = input("Please make your selection: ")

    # Open the 'task.txt' file, read the data, assign it to an array, and determine each task's index.
    out_file_task = open("tasks.txt", "r")
    text = out_file_task.read()
    task_array = text.split("\n")
    selected_task_arr = task_array[task_num - 1].split(", ")
    out_file_task.close()

    # If the user chose modify the completion status of the task, then only the tasks which has not yet been completed
    # can be changed from "no" to "yes".
    if user_option == "1":
        if name == selected_task_arr[0]:

            if selected_task_arr[-1] == "No":
                selected_task_arr[-1] = "Yes"
                print(f"Task: {selected_task_arr[1]}\nCompleted: {selected_task_arr[-1]}")
            else:
                print("This task has already been completed")

    # If the user selected the option to edit the user to whom the task is assigned, or change the completion date
    # of the task, then the program would prompt the user accordingly and request their input.
    else:
        if selected_task_arr[-1] == "No":
            print("1\t-\tEdit name\n2\t-\tChange completion date")
            user_selection = input("Please make your selection: ")
            # The new user for the tasks overrides the previous user.
            if user_selection == "1":
                new_user = input("Please enter the new user: ")
                selected_task_arr[0] = new_user
                print("Thank you. Your task has been changed")
                print(f"Task: {selected_task_arr[1]}\nNew user: {selected_task_arr[0]}")

            # The new completion date overrides the previous one.
            else:
                new_date = input("Please enter the new date: ")
                selected_task_arr[-2] = new_date
                print("Thank you. Your task has been changed")
                print(f"Task: {selected_task_arr[1]}\nNew date: {selected_task_arr[-2]}")
        else:
            print("This task has already been completed")

    # This script write the modifications back to the file.
    task_array[task_num - 1] = ", ".join(selected_task_arr)
    text = "\n".join(task_array)
    out_file_task = open("tasks.txt", "w")
    out_file_task.write(text)
    out_file_task.close()


# This function extracts the data that is to be used in the 'generate_report' function and convert the datat into
# statistics
def get_task_report(task_array):
    # Display the total number of tasks generated and tracked using this program
    report = f"The total number of tasks that have been generated and tracked is {len(task_array)}\n"

    # To count the number of tasks that have been completed, that have not been completed or that are overdue,
    # we assign their respective variables to zero.
    count_yes = 0
    count_no = 0
    count_overdue = 0

    # The program will loop through the text in the file, split each task in their own separate line, and read the last
    # entry to determine if the tasks has been completed with a "yes", not completed with a "no" or whether the task
    # is overdue by comparing it with the current date.
    for line in task_array:
        task = line.split(", ")
        if task[-1] == "Yes":
            count_yes += 1

        elif task[-1] == "No":
            count_no += 1

        if task[-1] == "No" and task[-2] > date.today().strftime("%d %b %Y"):
            count_overdue += 1

    # Display the total number of completed tasks
    report += f"The number of tasks completed is {count_yes}\n"

    # Display the total number of uncompleted tasks
    report += f"The number of tasks not completed is {count_no}\n"

    # Display the total number of overdue tasks
    report += f"The number of tasks that are overdue is {count_overdue}\n"

    # Display the percentage of incomplete tasks
    total_tasks = len(task_array)
    percentage_incomplete = round(count_no / total_tasks * 100, 2)
    report += f"{str(percentage_incomplete)}% tasks are incomplete\n"

    # Display the percentage of overdue tasks
    percentage_overdue = round(count_overdue / total_tasks * 100, 2)
    report += f"{str(percentage_overdue)}% tasks are overdue\n"
    return report


# This function assists the program to identify all the tasks assigned to a specific user.
def get_user_tasks(individual, all_tasks):
    # The user's tasks is assigned to an empty list, and in a for loop the program runs through all the tasks, splits
    # the first word of the task (which is the username), compares it to the user who signed in and if they match, the
    # program appends the task to the empty list.
    user_tasks = []
    for task_line in all_tasks:
        if individual == task_line.split(", ")[0]:
            user_tasks.append(task_line)
    return user_tasks


# The admin user can log in the program and generate statistical reports that are written to two files respectively.
def generate_report():
    # This function requires the input of the username, to ensure that the user can view the statistical results
    # of the tasks that are assigned to them.
    # Create and open writeable file named "task_overview"
    out_task_file = open('task_overview.txt', 'w')
    # Read the data in the task file and create an array of the tasks in the file.
    in_file_task = open("tasks.txt", "r")
    text = in_file_task.read().rstrip()
    in_file_task.close()
    task_array = text.split("\n")
    # Use the function that converted the data into statistics to write the data to the new file.
    overall_report = get_task_report(task_array)
    out_task_file.write(overall_report)
    out_task_file.close()

    # Create and open writeable file named "user_overview". This file will show only the statistics of the tasks related
    # to the user who signed in.
    out_user_file = open('user_overview.txt', 'w')

    in_file_user = open("user.txt", "r")
    text = in_file_user.read().strip()
    in_file_user.close()
    user_array = text.split("\n")

    # The total number of users registered with task_manager.py
    out_user_file.write(f"The total number of users that have been registered is {len(user_array)}\n")

    # Display the total number of tasks generated and tracked using this program
    out_user_file.write(f"The total number of tasks that have been generated and tracked is {len(task_array)}\n")

    # Use the function that generated statistics for each user's tasks
    for user in user_array:
        user_name = user.split(", ")[0]
        user_tasks = get_user_tasks(user_name, task_array)
        # Write the new data to a file in a readable format.
        out_user_file.write(f"Report for user {user_name}:\n{get_task_report(user_tasks)}\n")

    out_user_file.close()


# Display the information of the generated reports on the screen.
def display_stats():
    # Determine if the reports have been generated. If they cannot be found, then the program will first generate
    # the report.
    if not path.exists("task_overview.txt") or not path.exists("user_overview.txt"):
        generate_report()

    # Read the content of the task_overview file and display it on the screen.
    in_file_task = open("task_overview.txt", "r")
    text = in_file_task.read().strip()
    in_file_task.close()
    print(text)

    # Read the content of the user_overview file and display it on the screen.
    in_file_user = open("user_overview.txt", "r")
    data = in_file_user.read().strip()
    in_file_user.close()
    print(data)


# This is the main function where the user will be prompt to sign in, it will let the program continue to run, until
# the user decides to exit.
def main():
    print("Please login with your username and password")
    authenticated = False
    # Here we prompt the user repeatedly for their username and password, until the login attempt succeeds.
    while not authenticated:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        authenticated = sign_in(username, password)

    print('Your login has been approved.')

    # Call the selection function for the program to continue to the next step.
    while True:
        selection = get_selection(username)
        perform_action(selection, username)


# Call the main function to start the program.
main()

# Reference: https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
# Used this reference to append additional tasks and users to a file without overwriting the existing data.
# Reference: https://www.guru99.com/python-check-if-file-exists.html
# Used this reference to see how I can search whether a file can be found.

