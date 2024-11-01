from tkinter import *
from tkinter import ttk, messagebox
import pymongo

# I created this app to test MongoDB CRUD operations

# MongoDB connection
cluster = "mongodb+srv://tylermchambers92:Pyamp123@cluster.m2o0e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
client = pymongo.MongoClient(cluster)
db = client.TestDB
todos = db.ToDo

# get list of tasks from the DB
results = todos.find({})

root = Tk()
root.title("To-Do List")
# root.iconbitmap(r"cubeicon.ico")
root.geometry("500x325")
root.configure(background="green")

title_label = Label(root, text="To-Do List", font=("Brock Script", 20, "bold"), background="green",
                    padx=5)
title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

todo_tree = ttk.Treeview(root, columns=('Column 1', 'Column 2', 'Column 3'),
                         show='headings')

todo_tree.heading('Column 1', text='Urgency')
todo_tree.heading('Column 2', text='Task')
todo_tree.column("Column 1", width=75)
todo_tree.column("Column 2", width=200)

# Add data to tree from membership_type table
for result in results:
    todo_tree.insert('', 'end', values=(result['Urgency'], result['Task']))

todo_tree.grid(row=1, column=0, columnspan=5, rowspan=7, sticky="NEWS", pady=2)
tree_scroll = ttk.Scrollbar(root, orient="vertical", command=todo_tree.yview)
todo_tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.grid(row=1, column=5, rowspan=7, sticky="NS", pady=2)


def update_treeview():
    todo_tree.delete(*todo_tree.get_children())
    new_results = todos.find({})
    for new_result in new_results:
        todo_tree.insert('', 'end', values=(new_result['Urgency'], new_result['Task']))


def add_task():
    add_task_screen = Tk()
    add_task_screen.title("Add Task")
    # root.iconbitmap(r"cubeicon.ico")
    add_task_screen.geometry("325x100")
    add_task_screen.configure(background="green")

    fn_label = Label(add_task_screen, text="Urgency: ", background="green", padx=5)
    fn_label.grid(row=0, column=0, sticky="W", pady=2, padx=2)
    fn_entry = Entry(add_task_screen, width=40)
    fn_entry.insert(0, "Enter Urgency 1(highest)-10")
    fn_entry.grid(row=0, column=1, columnspan=2, sticky="W", pady=2)

    bn_label = Label(add_task_screen, text="Task: ", background="green", padx=5)
    bn_label.grid(row=1, column=0, sticky="W", pady=2, padx=2)
    bn_entry = Entry(add_task_screen, width=40)
    bn_entry.insert(0, "Take out the groceries...etc")
    bn_entry.grid(row=1, column=1, columnspan=2, sticky="W", pady=2)

    def add():
        body = {
            "Urgency": fn_entry.get(),
            "Task": bn_entry.get()
        }

        try:
            todos.insert_one(body)
            update_treeview()
            messagebox.showinfo('Task Added', 'Task had been added')
            add_task_screen.withdraw()
            add_task_screen.quit()
        except Exception as error:
            messagebox.showinfo('Error', f"{error}")
            add_task_screen.withdraw()
            add_task_screen.quit()

    add_task_button = Button(add_task_screen, text="Add Task", command=add)
    add_task_button.grid(row=3, column=1, sticky="EW", pady=2, padx=5)

    def cancel():
        add_task_screen.withdraw()
        add_task_screen.quit()

    remove_task_button = Button(add_task_screen, text="Cancel", command=cancel)
    remove_task_button.grid(row=3, column=2, sticky="EW", pady=2, padx=5)

    add_task_screen.mainloop()


add_button = Button(root, text="Add", command=add_task)
add_button.grid(row=8, column=0, sticky="EW", pady=2, padx=5)


def remove_task():
    current_item = todo_tree.focus()
    highlighted_row = todo_tree.item(current_item)
    urgency = highlighted_row["values"][0]
    task = highlighted_row['values'][1]
    todos.delete_one({"Urgency": urgency, "Task": task})
    update_treeview()


remove_button = Button(root, text="Remove", command=remove_task)
remove_button.grid(row=8, column=2, sticky="EW", pady=2, padx=5)


def update_task():
    current_item = todo_tree.focus()
    highlighted_row = todo_tree.item(current_item)
    urgency = highlighted_row["values"][0]
    task = highlighted_row['values'][1]

    update_task_screen = Tk()
    update_task_screen.title("Update Task")
    # root.iconbitmap(r"cubeicon.ico")
    update_task_screen.geometry("325x100")
    update_task_screen.configure(background="green")

    cn_label = Label(update_task_screen, text="Urgency: ", background="green", padx=5)
    cn_label.grid(row=0, column=0, sticky="W", pady=2, padx=2)
    cn_entry = Entry(update_task_screen, width=40)
    cn_entry.insert(0, f"{urgency}")
    cn_entry.grid(row=0, column=1, columnspan=2, sticky="W", pady=2)

    dn_label = Label(update_task_screen, text="Task: ", background="green", padx=5)
    dn_label.grid(row=1, column=0, sticky="W", pady=2, padx=2)
    dn_entry = Entry(update_task_screen, width=40)
    dn_entry.insert(0, f"{task}")
    dn_entry.grid(row=1, column=1, columnspan=2, sticky="W", pady=2)

    def update():
        try:
            todos.update_one({"Task": task}, {"$set": {"Urgency": cn_entry.get(),
                                                       "Task": dn_entry.get()}})
            update_treeview()
            messagebox.showinfo('Task Updated', 'Task had been updated')
            update_task_screen.withdraw()
        except Exception as error:
            print(error)
            messagebox.showinfo('Error', f"{error}")
            update_task_screen.withdraw()
            update_task_screen.quit()

    add_task_button = Button(update_task_screen, text="Update Task", command=update)
    add_task_button.grid(row=3, column=1, sticky="EW", pady=2, padx=5)

    def cancel2():
        update_task_screen.withdraw()
        update_task_screen.quit()

    remove_task_button = Button(update_task_screen, text="Cancel", command=cancel2)
    remove_task_button.grid(row=3, column=2, sticky="EW", pady=2, padx=5)


update_button = Button(root, text="Update", command=update_task)
update_button.grid(row=8, column=1, sticky="EW", pady=2, padx=5)

root.mainloop()
