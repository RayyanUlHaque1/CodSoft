# To-Do List Application
This To-Do List application is built using Python's Tkinter library.
It allows users to manage their tasks with a simple and intuitive interface. 
Users can add, remove, mark tasks as done, and save/load their task list from a file.

# Features
Add Task: 
Users can enter a task in the input field and click "Add Task" to add it to the task list.

Remove Task: 
Users can select a task from the list and click "Remove Task" to delete it from both the list and the application.

Mark Task as Done: 
Users can select a task from the list and mark it as done by clicking "Task Done". This will prepend a checkmark symbol ("✔️") to the task.

Save Task List: 
Users can save the current list of tasks to a file so that it persists between sessions.

Load Task List: 
Users can load a previously saved task list from a file to restore their tasks.

# Functionalities
1. add_task()
This function is triggered when the "Add Task" button is clicked.
It retrieves the task entered in the input field, adds it to the global todo_list, and updates the Listbox to display the new task.
The input field is then cleared to allow for the next task to be entered.
2. remove()
This function is triggered when the "Remove Task" button is clicked.
It removes the selected task from both the todo_list and the Listbox.
3. done()
This function is triggered when the "Task Done" button is clicked.
It marks the selected task as done by adding a checkmark ("✔️") at the beginning of the task string.
The updated task is then replaced in the todo_list and the Listbox.
4. save()
This function is triggered when the "Save Task" button is clicked.
It saves the current todo_list (a list of tasks) to a file (todo_list.pk1) using Python's pickle module for persistence.
5. load()
This function is triggered when the "Load Task" button is clicked.
It attempts to load the saved todo_list from the file (todo_list.pk1).
If the file exists, it updates the Listbox with the saved tasks.
If the file doesn't exist (e.g., no saved tasks), it prints a message indicating that no tasks were found.
# Graphical User Interface (GUI)
The application uses Tkinter to create a GUI with the following elements:

Title: A large title at the top of the window ("Your To-Do-List").
Task Entry: A text input field where users can enter tasks.
# Buttons:
"Add Task" to add tasks.
"Remove Task" to remove selected tasks.
"Task Done" to mark tasks as done.
"Save Task" to save tasks.
"Load Task" to load saved tasks.
# Task Listbox: 
A list box that displays the current tasks, allowing users to select and interact with them.
The interface is styled with a calming color scheme, and the font choices aim for readability and clarity.

# Code Overview
The application uses the Tkinter library for the GUI, along with the pickle module to handle task list persistence.
todo_list is a global variable that holds all tasks in the application. Tasks are stored as strings in this list.
Each task is represented as a string, with completed tasks marked with a checkmark symbol ("✔️") at the beginning of the task.
# How to Use
1. Adding Tasks: Enter a task in the input field and click "Add Task" to add it to the list.
2. Removing Tasks: Select a task from the Listbox and click "Remove Task" to delete it.
3. Marking Tasks as Done: Select a task and click "Task Done" to add a checkmark ("✔️") to the task.
4. Saving Tasks: Click "Save Task" to save the current task list to a file.
5. Loading Tasks: Click "Load Task" to load a previously saved task list.


# Notes
The task list is saved to a file named todo_list.pk1 in the same directory as the script. If the file does not exist, tasks will not be loaded when the application is started.
Tasks marked as done will be displayed with a checkmark symbol ("✔️") at the beginning of the task.