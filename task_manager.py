# This program is designed for a small business to help it to manage tasks assigned to each member of a team
# First the user must login into the programme
# There is a text file with all the current users 
# The tasks are stored in a separate text file
# If the login is successful the user is prompted to the menu to select a task
# The admin user will be given an additional menu list 

# Import the datetime and date from datetime module to access the date
from datetime import datetime, date
# Constant variable
DATETIME_STRING_FORMAT = ' %d %m %Y'

# Main Programme
print("\n=================== MAIN PROGRAM ===================\n")

# Code to print the MENU OPTIONS
def menu_options():                 
    print("\n=================== MAIN OPTIONS ===================\n")
    print("\nPlease select one of the following options:\n")
    print("\tr   - Register User")
    print("\ta   - Add Task")
    print("\tva  - View All Tasks")
    print("\tvm  - View My Yasks")
    print("\tgr  - Generate Reports")
    print("\te   - Exit")
    print("\n=================== END MENU ===================")

# Code to REGISTER USER
def reg_user():                     
    print("\nRegister a New User option selected.\n") # Prints the welcoming message    
    with open('user.txt', 'r', encoding='utf-8') as user_file:  # Code to open user file in read mode
        new_username = input("Enter a new username: ") # Code to register a new user's input

        user_new = False
        username_list = [] # Username list
        for line in user_file: # Code to manipulate the user text file
            line = line.split(",") 
            user = line[0]
            username_list.append(line[0])

        while user in username_list: # Code to check if user exists already in the system
            if new_username not in username_list: # If new user then continue to next step
                break
            elif user in username_list: # Code to allert the user's existence login
                print("Username already exists!")
                new_username = input("Enter a new username: ") # Try to login with new input
                      
        new_password = input("Enter the password: ") # Code to store the password
        confirm = input("Confirm password: ") # Confirm the password

    with open('user.txt', 'a', encoding='utf-8') as user_file: # Code to open user file in append mode
        if new_password == confirm: # Code to check the password
            new = f"\n{new_username}, {new_password}"     
            user_file.write(new) # Store the new user credentials
            print("\nNew User added") # Confirm the user's input
        else:
            print("\nPasswords do not match.") # Error message for wrong password
                
        if main_menu == "r" and logged_in != "admin":
            print("Registering new users requires admin privileges") # Error message for wron admin selection

# Code to ADD A TASK
def add_task():                                
    print("\nAdd New Task option selected.\n")
    with open('tasks.txt', 'a', encoding='utf-8') as task_file: # Open the tasks.txt to append a new task      
        task = 0
        tasks = int(input("\nEnter the number of tasks you'd like to add: ")) # Range of number of tasks selected by the user
        for task in range (tasks):
            user = input("\nEnter the name of the person the task is assigned to: ") # Assign the task to a user
            title = input("Enter the title of task: ") # Create a task name
            description = input("Enter the task description: ") # Store the new task description
            assign_date = date.today()            
            due_date = input("Due date of task (DD MM YYYY)): ") # Store the due date of the task
            new_task = f"\n{user}, {title}, {description}, {due_date}, {assign_date.strftime(DATETIME_STRING_FORMAT)}, No" # Prints all the user's new task input
            task_file.write(new_task) # Write the info collected to task file
        print("\nYou have successfully added task(s).")       

# Code to VIEW ALL TASKS
def view_all():                          
    print("\nView All tasks information option selected.\n")
    key_start = 0
    tasks_list = [] # List of tasks
    tasks_dict = {} # Dictionary of tasks
    # Opens tasks file in read mode
    task_file = open('tasks.txt', 'r', encoding='utf-8')    
    # Code to manipulate info in text file       
    for line in task_file:                      
        line = line.strip("\n")
        tasks_info = line.split(",")
        key_start += 1
        tasks_list = tasks_info
        (key, value) = key_start, tasks_info 
        tasks_dict[key] = tasks_info         
        # Code to displays all the information  
        print("Task No:\t\t ", key_start)       
        print("Title:\t\t\t", tasks_list[1])
        print("Assigned to:\t\t ", tasks_list[0])
        print("Date Assigned:\t\t", tasks_list[3])
        print("Due Date:\t\t", tasks_list[4])
        print("Task Complete:\t\t", tasks_list[5])
        print("Task Description:\t",tasks_list[2])
        print("\n=================== END OPTION ===================")

# Code to print information for the CURRENT USER
def view_mine():                                
    print("\nYou have selected to View your task information\n")
    # Opens tasks text file in read mode
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:   
        key_start = 0
        tasks_list = []                     
        tasks_dict = {}                       
        # Code to manipulate info in text file    
        for line in task_file:
            line = line.strip("\n")             
            tasks_info = line.split(",")
            key_start += 1
            tasks_list = tasks_info # Updated list     
            (key, value) = key_start, tasks_info 
            tasks_dict[key] = tasks_info # Updated dictionary
            # Prints the information of the current user
            if logged_in == tasks_list[0]:    
                print("Task No:\t\t ", key_start)
                print("Title:\t\t\t", tasks_list[1])
                print("Assigned to:\t\t ", tasks_list[0])
                print("Date Assigned:\t\t", tasks_list[3])
                print("Due Date:\t\t", tasks_list[4])
                print("Task Complete:\t\t", tasks_list[5])
                print("Task Description:\t",tasks_list[2])
                print("\n=================== END OPTION ===================\n")

# Code to DISPLAY ADMIN OPTIONS
def admin_options():                           
                                 
    print("\nAdmin Menu, please select one of the following options:\n")
    print("\tds  - Display Statistics")
    print("\tau  - Create a New User in users' file")
    print("\tat  - Create a New Task in tasks' file")
    print("\ts   - To skip this menu and go to the next")
    print("\n=================== END OPTION ===================\n")

# Code to ADD NEW USER
def add_user():                                
    print("\nAdd New User option selected.\n")
    # Opens user file in append mode to add a new user
    with open('user.txt', 'a', encoding='utf-8') as user_file:             
        user_file.write("\n")                  
        credentials = False
                      
        i = 0
        team_members = int(input("\nEnter the number of users you'd like to add: "))      
        # Code to get login details for the specified number of users
        for i in range(team_members):                      
            username = input("\nCreate a username: ")
            print("\nPlease note password should contain 5 or more characters, any characters and at least one number.")
            password = input("Please enter a password: ")
                      
            # Code to check the password validity
            length = input("\nIs your password 5 characters long or more?: (Yes/No) ")
            characters = input("Does your password contain small case characters? (Yes/No) ")
            digit = input("Does your password contain at least one digit? (Yes/No) ")
            # Accepted and stored password
            if length == "Yes" and characters == "Yes" and digit == "Yes":            
                credentials = True
            # Code to confirm user credential
            if credentials == True:                  
                assignment = f"{username}, {password}"         
                user_file.write(assignment)                     
                      
                print("\nYou have successfully created login credentials.")
            # Code if password credentials are not met
            if length != "Yes" or characters != "Yes" or digit != "Yes": # Failed conditions for creating a password 
                credentials == False                  
                print("\nThe password you have entered is not accepted, try another password.")

# Code to DISPLAY STATISTICS
def display_statistics():               
    print("\nYou have selected to Display Statistics\n")                
    # Opens user file in read mode       
    with open('task_overview.txt', 'r', encoding='utf-8') as f_task:  
        # Code to manipulate the text file     
        for line in f_task:             
            line = line.strip("\n")
            # Code to display the total number of tasks from text file
            if line.startswith("Total"):    
                line = line.split(":")
                tasks_count = line[1]
        print(f"\nThe total count of tasks is: {tasks_count}")

    # Opens user file in read mode
    with open('user_overview.txt', 'r', encoding='utf-8') as f2_task:         
        for line in f2_task:
            line = line.strip("\n")
    
            if line.startswith("Total Users"):  
                line = line.split(":")
                user_count = line[1]
        print(f"\nThe total count of users is: {user_count}") # Total number of users from text file

    with open('task_overview.txt', 'r', encoding='utf-8') as f_task:
        print("\nALL TASKS REPORTS \n") # Prints all the file info
        for line in f_task:
            line = line.strip("\n")
            print(line)
            
    # Opens user file in read mode
    with open('user_overview.txt', 'r', encoding='utf-8') as f2_task:         
        print("\nALL USERS REPORTS \n") # Prints all the file info
        for line in f2_task:
            line = line.strip("\n")
            print(line)
            
# Code to manipulate text file to update any changes or edits from the user 
def file_edit():                            
    task_edit = open('tasks.txt', 'r+') # Opens file then reads
    lines = task_edit.readlines()
    task_edit.close()
    del lines[task_selection-1] # Code to delete a specific line that corresponds to task that user is editing
                    
    task_edit_write = open('tasks.txt', 'w+') # Opens file in write mode
    for line in lines:
        task_edit_write.write(line)  # write updated file 
    task_edit_write.close()

    task_edit_new = open('tasks.txt', 'a') # Opens file as append mode
    task_edit_new.write(f"\n{select_list[0]}, {select_list[1]}, {select_list[2]}, {select_list[3]}, {select_list[4]}, {select_list[5]}") # Adds new edited task
    task_edit_new.close()

# LOGIN SECTION
login = False                                 

with open('user.txt', 'r', encoding='utf-8') as user_file: # Opens user file in read mode
    contents = user_file.read()                                 
    contents = contents.replace(",", "").split()     
    # Initializing welcoming message
    print("Welcome to TASK MANAGER! ") 
    login_username = input("\nEnter your username: ") # Asks the user for username 
    login_password = input("Enter your password: ") # Asks the user for password
    
    
    login_check = True                   
    while login_check:                
        for line in contents:          
        #Check if username and password matches file info
            if line.startswith(login_username) and line.endswith(login_password):  
                login = True 
                login_check = False          
                logged_in = login_username # The user logged in successfully
                print(f"\nYou have successfully logged in, welcome {logged_in}.")

        if login_check: # Message if login details do not match
            print("\nInvalid username or password. Please try again.")
            login_username = input("\nEnter your username: ")
            login_password = input("\nEnter your login password: ")

    
    # Code for ADMIN USER LOGIN 
    if logged_in == "admin":                 
        admin_options()                         

        admin_menu = input("\nSelect an option from the menu above before you can access the main menu: ") # Option selection for admin user
        if admin_menu == "au": # Option to add new user to text file 
            add_user()
        
        elif admin_menu == "at": # Option to write new task 
            add_task()                
            
        elif admin_menu == "ds": # Option to display statistics 
            display_statistics()
                         
        elif admin_menu == "s": # Option to skip to next menu
            pass
        else:
            print("Invalid selection")

# Code for USER LOGIN           
if login:
    menu_options()

#Tasks information  
    key_start = 0 
    tasks_list = []          
    tasks_dict = {}                   
    # Opens tasks file in read mode
    with open('tasks.txt', 'r', encoding='utf-8') as task_file: 
        # Code to manipulate info in text file        
        for line in task_file:         
            line = line.strip("\n")
            tasks_info = line.split(",")
            key_start += 1
            tasks_list = tasks_info
            (key, value) = key_start, tasks_info 
            tasks_dict[key] = tasks_info # Updated dictionary

 
    # Users Information
    count = 0                           
    users_dict = {}                    
    # Opens user file in read mode
    with open('user.txt', 'r', encoding='utf-8') as user_file:        

        for username in user_file:
            count += 1
            contents = username.split(',')
            contents = contents[0]
            # Code to update user dictionary
            users_dict[count] = contents      
        users_list = users_dict.values()

    # Menu options 
    main_menu = input("\nSelect an option from the Main Menu: ")     
    # Options available only for 'admin' user 
    if main_menu == "r" and logged_in == "admin":               
        reg_user()
        
    elif main_menu == "a": # Add task                         
        add_task()

    elif main_menu == "vm": # View current user tasks                      
        view_mine()

    elif main_menu == "va": # View all tasks                    
        view_all()


        # Code to allow the user to select a specific task from all tasks
        task_selection = int(input("\nSelect a task by entering corresponding number: "))     
        valid_selection = False
        # user input ‘-1’ to return to the main menu.
        while task_selection != -1:                         
            if task_selection in tasks_dict:
                select_list = tasks_dict[task_selection]
                valid_selection = True
                # Code is allowing the user to edit the selected task
                print("\nm\t- Mark task as complete")       
                print("e\t- Edit task")
                print("c\t- cancel")
                # Select action
                action = input("\nSelect an action to perform: ")  
                if select_list[5] == " Yes":                
                    print("\nTask has already been completed and it cannot be edited!")
                    break
                # action to store as complete
                if action == "m" and select_list[5] != " Yes":  
                    select_list[5] = " Yes"
                    print(f"\nTask {task_selection} is now marked as complete")
                    tasks_dict[task_selection] = select_list                   
                    file_edit()                   
                    break

                 # Edits the task infomation
                elif action == "e" and select_list[5] != " Yes":   
                    select_list = tasks_dict[task_selection]
                    # Edits selection option
                    further_select = input("What task information you'd like to edit? (User, Due date, Both) or c to cancel: ")

                    if further_select == "User":
                        select_list[0] = input("Edit user name: ")
                        print(f"\nTask {task_selection} is now assigned to {select_list[0]}")

                    elif further_select == "Due date":
                        select_list[4] = input("\nEdit due date, format DD MM YYYY: ")
                        print(f"\nThe due date for task {task_selection} is now {select_list[4]}")

                    elif further_select == "Both":
                        select_list[0] = input("Edit user name: ")
                        select_list[4] = input("\nEdit due date, format DD MM YYYY: ")
                        print(f"\nTask {task_selection} is now assigned to {select_list[0]} and the new due date is {select_list[4]}")

                    elif further_select == "c":
                        pass
                    else:
                        print("Invalid selection!")
                    
                    tasks_dict[task_selection] = select_list
                    file_edit()
                    break
                elif action == "c":                                 #if user does not want to edit, user can skip by 'cancelling'
                    break

            elif task_selection not in tasks_dict: 
                valid_selection = False
            print("Invalid task selection")
            break
                   
    # Code to generate and display reports   
    elif main_menu == "gr":
        print("\nYou have selected to Generate Reports\n")
        # Create and modify tasks/user files 
        f1 = open('task_overview.txt', 'w', encoding='utf-8')                         
        f2 = open('user_overview.txt', 'w', encoding='utf-8')
        f1.write("Tasks information:\n")
        
        # For the Tasks Overview file:
        all_tasks = len(tasks_dict)    
        value = 0
        complete_count = 0
        incomplete_count = 0
        # Loops through the tasks dictionary
        for value in tasks_dict:                            
            separate_list = tasks_dict[value]      
            # Complete task
            if separate_list[5] == " Yes":          
                complete_count += 1
            # Incomplete task   
            elif separate_list[5] == " No":      
                incomplete_count += 1
         # Percentage of task completion       
        percent_incomplete =  round((incomplete_count/ len(tasks_dict) * 100), 2) 

        # Displays all the information
        print("\nTask Overview")
        print("(NB: Admin can access these numbers in detail)")
        print("\nTotal number of tasks: ", all_tasks)
        print("Total number of complete tasks: ", complete_count)
        print("Total number of incomplete tasks: ", incomplete_count)
        
        # Overdue tasks
        overdue_count = 0
        for value in tasks_dict:                           
            separate_list = tasks_dict[value]
            date_today = date.today()                       
            due_date = datetime.strptime(separate_list[4], DATETIME_STRING_FORMAT) # Store the date 
            due_date = due_date.date()
            # Compare the dates
            if due_date < date_today and separate_list[5] == " No":    
                overdue_count += 1
                    
        # Display tasks completion percentage
        percent_overdue = round((overdue_count/ len(tasks_dict) * 100), 2)  
        print("Number of overdue tasks is: ", overdue_count)
        print("Percentage of incomplete tasks: ", percent_incomplete)
        print("Percentage of overdue tasks: ", percent_overdue)

        # Code to write info from generate reports to output file, Tasks_Overview
        f1.write(f"Total: {all_tasks}")
        f1.write(f"\nCompleted: {complete_count}")
        f1.write(f"\nIncomplete: {incomplete_count}")
        f1.write(f"\nOverdue: {overdue_count}")
        f1.write(f"\nPercentage Incomplete: {percent_incomplete}%")
        f1.write(f"\nPercentage Overdue: {percent_overdue}%")

       # Code to generate report from users information:
        total_users = len(users_dict)                      
        all_tasks = len(tasks_dict)                         
        
        print(f"\nTotal number of users is: {total_users}\n")  
        print(f"Total number of tasks is: {all_tasks}")

        # Code to write information to User_Overview 
        f2.write(f"Users Information:\n")                  
        f2.write(f"Total Users: {total_users}\n")
        f2.write(f"Total Tasks: {all_tasks}\n")


        # Initialise start values for tasks
        user_count = 0
        user_overdue = 0
        user_complete = 0
        user_complete_perc = 0
        user_overdue = 0

        print("\nUser Overview:")                    
        print("(NB: Admin can access these numbers in detail)")
        # Code for each user in the dictionary and for corresponding task
        for user in users_dict.values():                    
            for value in tasks_dict:
                separate_list = tasks_dict[value]
                
                if separate_list[0] == user:
                    user_count += 1
                    
                    if user_count == 0:   # No tasks are assigned to user
                        user_count = 0.00000000000000000001 # Divide by a negligible number to avoid dividing by 0
                        
                    percent_assigned = round((user_count/len(tasks_dict)*100), 2)

                    if separate_list[5] == " Yes":
                        user_complete += 1

                    if separate_list[5] == " No":
                        date_today = date.today()
                        due_date = datetime.strptime(separate_list[4], DATETIME_STRING_FORMAT)
                        due_date = due_date.date()
                        # Compares dates in input file with curent date to see if overdue
                        if due_date < date_today:    
                            user_overdue += 1
            # Code to find the user's completed tasks percentage
            if user_count == 0: # No tasks assigned to user 
                        user_count = 0.00000000000000000001 # Divide by a negligible number to avoid dividing by 0 
            user_complete_perc = round((user_complete/user_count*100), 2)
            user_to_complete = 100 - user_complete_perc
            perc_user_overdue = round((user_overdue/ user_count * 100), 2)
            
            # Display all the user's information          
            print(f"\n{user}: \n")
            print(f"Number of tasks assigned to {user} are: {user_count}\n")
            print(f"Percentage of tasks assigned to {user} is: {percent_assigned}\n")
            print(f"Completed tasks by {user} are: {user_complete}\n")
            print(f"Percentage of completed tasks by {user} is: {user_complete_perc}\n")
            print(f"Percent of tasks to be completed by {user} is: {user_to_complete}\n")
            print(f"Number of {user}'s overdue tasks is: {user_overdue}\n")
            print(f"Percentage of {user}'s overdue tasks is: {perc_user_overdue}\n")
            print("\n=================== END OPTION ===================\n")
            # Code to write the information from generate reports to output file User_Overview          
            f2.write(f"\nUser: {user}\n")
            f2.write(f"Tasks Assigned: {user_count}\n")
            f2.write(f"Percentage Assigned: {percent_assigned}%\n")
            f2.write(f"Percentage Completed: {user_complete_perc}%\n")     
            f2.write(f"Percentage Incompleted: {user_to_complete}%\n")
            f2.write(f"Percentage Overdue: {perc_user_overdue}%\n")
            print("\n=================== END OPTION ===================\n")
            # Reset all the counts and the same variable for each user's count           
            user_count = 0            
            percent_assigned = 0
            user_overdue = 0
            user_complete = 0
            user_complete_perc = 0
            user_overdue = 0
            perc_user_overdue = 0
        # Closes file
        f1.close()                      
        f2.close()
        
    #iCode to check for logged in user, option available only to an admin   
    elif main_menu == "ds":       
        if logged_in == "admin":
            pass
        else:
            print("Option only available to admin user! Login as admin to view Statistics.")
            
    # Code to exit the program
    elif main_menu == "e":                           
            exit(0)                                          
       
    elif main_menu == "r" and logged_in != "admin":     # Displays error message if other user tries to access
        print("Option only available to admin user! Login as admin to register user")

    # Code for invalid selection   
    elif main_menu != "r" or main_menu != "a" or main_menu != "vm" or main_menu != "va" or main_menu != "e":      
        print("\nInvalid selection!")
