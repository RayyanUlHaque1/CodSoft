from tkinter import Tk, Label, Entry, StringVar, Button, Listbox, END
import pickle

# Global task list
todo_list = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        list_box.insert(END, task)
        task_entry.delete(0, END)

# Function to remove a task
def remove():
    selected_task = list_box.curselection()
    if selected_task:
        # Get the task and delete it from both the list and the Listbox
        task = list_box.get(selected_task)
        todo_list.remove(task)
        list_box.delete(selected_task)

# Function to mark a task as done
def done():
    selected_task = list_box.curselection()
    if selected_task:
        task = list_box.get(selected_task)
        if not task.startswith('✔️'):  # If not already marked
            task = '✔️ ' + task  # Mark as done by adding checkmark
            todo_list[todo_list.index(list_box.get(selected_task))] = task  # Update the list
            list_box.delete(selected_task)
            list_box.insert(selected_task, task)  # Insert back the updated task

# Function to save the task list
def save():
    with open('todo_list.pk1', 'wb') as f:
        pickle.dump(todo_list, f)

# Function to load the task list
def load():
    global todo_list  # Ensure we're modifying the global todo_list
    try:
        with open('todo_list.pk1', 'rb') as f:
            todo_list = pickle.load(f)  # Correctly load the list from pickle
        # Clear the Listbox and reinsert tasks
        list_box.delete(0, END)
        for task in todo_list:
            list_box.insert(END, task)
    except FileNotFoundError:
        print("No saved tasks found!")

# Create the main window
win = Tk()
win.title("To-Do-List")
win.state('zoomed')
win.resizable(width=False, height=False)
win.configure(bg="#387478")

# Header
title = Label(win, font=('Arial', 37, 'bold'), text='My To-Do-List', bg='#387478', fg='#E2F1E7')
title.pack(pady=10)

# Entry for task title
task_entry_lab = Label(win, font=('Arial', 32, 'bold'), text='Enter Task:', bg='#387478', fg='#E2F1E7')
task_entry_lab.place(relx=.42, rely=.18)

text_var = StringVar()
task_entry = Entry(win, width=55, textvariable=text_var, font=('Arial', 15, 'bold'),bg='#629584',fg='#E2F1E7',bd=3)
task_entry.place(relx=.31, rely=.25)
task_entry.focus()

# Buttons
add_button = Button(win, text='Add Task', width=12, font=('Arial', 15, 'bold'), bd=2, bg='#243642', fg='#E2F1E7', command=add_task)
add_button.place(relx=.32, rely=.35)

remove_button = Button(win, text='Remove Task', width=12, font=('Arial', 15, 'bold'), bd=2, bg='#243642', fg='#E2F1E7', command=remove)
remove_button.place(relx=.59, rely=.35)

done_button = Button(win, text='Task Done', width=10, font=('Arial', 15, 'bold'), bd=2, bg='#243642', fg='#E2F1E7', command=done)
done_button.place(relx=.46, rely=.4)

save_button = Button(win, text='Save Task', width=12, font=('Arial', 15, 'bold'), bd=2, bg='#243642', fg='#E2F1E7', command=save)
save_button.place(relx=.32, rely=.45)

load_button = Button(win, text='Load Task', width=12, font=('Arial', 15, 'bold'), bd=2, bg='#243642', fg='#E2F1E7', command=load)
load_button.place(relx=.59, rely=.45)

# Listbox to display tasks
list_label=Label (win,text='Tasks:',font=('Arial',23,'bold'),bg='#387478',fg='#E2F1E7')
list_label.place(relx=.48,rely=.50)
list_box = Listbox(win, height=14, width=33  ,bg='#629584',font=('Arial',15,'bold'),fg='white',bd=4)
list_box.place(relx=.39, rely=.55)

# Start the Tkinter event loop
win.mainloop()
