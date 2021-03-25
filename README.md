# taskManager
A simple program that lets user manage tasks created and assigned to other users

This task manager allows the user to select one of the following functions:
1. Register a user
1. Add a task
1. View all the tasks that have been created
1. View only the tasks assigned to the user who logged in
1. Modify tasks, i.e mark them as complete or edit the due date. 
1. The admin user can generate reports of all the users who are registered and the tasks assigned to them
1. The admin user can also view the stats of all the tasks

The program starts by asking the user for their username and password. It then checks against the file with the saved registered users whether the user exists and if the password matches the user's input. 

Once the user has logged in, the program displays a menu from which the user can select by entering the relevant letter associated with the function. If the admin user logged in, they will be able to see two additional functions that are not visible to the other users such as "generate reports" and "display statistics". 

To register a new user, the user should provide the new username and a password. The program first checks against the user file whether the user already exists. If the new username has not been found, then the user can continue to to enter the new password and confirm it by retyping the password. If it does not matches, the program will provide an error message accordingly and prompt the user to enter the password again. If it matches then the new user has been registered. The user file is updated with the new information. 

When the user want to register a new task, the program will given them instructions on what input is required. The task is saved to the task file. 

The user can view all the tasks that are in the task file. When selecting this option, the program reads the file and displays the information in a readable format on the IDE. 

Alternatively, the user can view only the tasks assigned to them. The program reads the user who signed in and displays the tasks in a readable format on the IDE. In this function, the user can select a specific task which they can either mark as complete or edit the task. Note, the user can only modify tasks that does not have a "complete" status. 

When the admin user selects 'generate report' the program extracts the date from the task file and displays the total number of tasks that have been generated. It also counts the tasks that have been completed, that have not been completed and that are overdue. It also display this statistics in percentage. 

The admin user can also log in the program and generate statistical reports that are written to two files respectively, namely 'task_overview' and user_verivew'. The program will also display the information that was written to the files on the IDE screen.

This program is useful to keep track of various users assigned to different tasks. Basic information of the tasks are required and tasks can be modified. Users can keep track of their tasks assigned to them and the admin user can have an overview of all the tasks assigned and all the users who are registered. 

The author of this code is the sole contributor and maintains the code. 

User can run the code on any IDE. 
