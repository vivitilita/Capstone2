# task-manager
Another milestone - second capstone project.
This is a program designed for a small business to help it to manage tasks assigned to each member of a team.
### The main menu:

+ reg_user — that is called when the user selects ‘r’ to register a user.
+ add_task — that is called when a user selects ‘a’ to add a new task.
+ view_all — that is called when users type ‘va’ to view all the tasks
listed in ‘tasks.txt’.
+ view_mine — that is called when users type ‘vm’ to view all the tasks that have been assigned to them.
  + when the user selects ‘vm’ to view all the tasks assigned to them:
      * Display all tasks in a manner that is easy to read. Make sure that each task is displayed with a corresponding number which can be used to identify the task.
      * Allow the user to select either a specific task (by entering a number) or input ‘-1’ to return to the main menu.
      * If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task. If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that describes whether the task has been completed or not should be changed to ‘Yes’. 
      * When the user chooses to edit a task, the username of the person to whom the task is assigned or the due date of the task can be edited. The task can only be edited if it has not yet been completed.
+ Add an option to generate reports to the main menu of the application:
>> When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt, should be generated. Both these text files should output data in a user-friendly, easy to read manner.
  + task_overview.txt should contain:
    * The total number of tasks that have been generated and tracked using the task_manager.py.
    * The total number of completed tasks.
    * The total number of uncompleted tasks.
    * The total number of tasks that haven’t been completed and
that are overdue. 
    * The percentage of tasks that are incomplete.
    * The percentage of tasks that are overdue.
  + user_overview.txt should contain:
    * The total number of users registered with task_manager.py.
    * The total number of tasks that have been generated and
tracked using task_manager.py.
    * For each user also describe:
      * The total number of tasks assigned to that user.
      * The percentage of the total number of tasks that have
been assigned to that user
      * The percentage of the tasks assigned to that user that
have been completed
      * The percentage of the tasks assigned to that user that
must still be completed
      * The percentage of the tasks assigned to that user that
have not yet been completed and are overdue
+ Modify the menu option that allows the admin to display statistics so that the reports generated are read from task _overview.txt and user_overview.txt and displayed on the screen in a user-friendly manner. If these text files don’t exist (because the user hasn’t selected to generate them yet), first call the code to generate the text files.


### Key learnings:
- [x] Working with while/for loops
- [x] Data structures: lists/ dictionaries
- [x] Defining functions
- [x] Working with external data structures I/O 



