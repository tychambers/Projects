from tkinter import *
from tkinter import font, ttk, messagebox
from functions import ConnectionSQL


class MySQLConnection:
    def __init__(self):
        self.host = ""
        self.database = ""
        self.username = ""
        self.password = ""

    def connect_to_db(self):
        root = Tk()
        root.title("Connect to DB")
        root.iconbitmap(r"cubeicon.ico")
        root.geometry("280x180")
        root.configure(background="grey")

        connection_sql = ConnectionSQL()

        title_label = Label(root, text="Connect to MySQL", font=("Arabic Transparent", 20, "bold"), background="grey",
                            padx=5)
        title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

        host_label = Label(root, text="Host Address: ", background="grey", padx=5)
        host_label.grid(row=1, column=0, sticky="W", pady=2, padx=2)
        host_entry = Entry(root, width=20)
        host_entry.insert(0, "localhost")
        host_entry.grid(row=1, column=1, columnspan=2, sticky="W", pady=2)

        db_label = Label(root, text="Database Name: ", background="grey", padx=5)
        db_label.grid(row=2, column=0, sticky="W", pady=2, padx=2)
        db_entry = Entry(root, width=20)
        db_entry.insert(0, "testdb")
        db_entry.grid(row=2, column=1, columnspan=2, sticky="W", pady=2)

        un_label = Label(root, text="Username: ", background="grey", padx=5)
        un_label.grid(row=3, column=0, sticky="W", pady=2, padx=2)
        un_entry = Entry(root, width=20)
        un_entry.insert(0, "root")
        un_entry.grid(row=3, column=1, columnspan=2, sticky="W", pady=2)

        pw_label = Label(root, text="Password: ", background="grey", padx=5)
        pw_label.grid(row=4, column=0, sticky="W", pady=2, padx=2)
        pw_entry = Entry(root, width=20)
        pw_entry.insert(0, "Pyamp123!")
        pw_entry.grid(row=4, column=1, columnspan=2, sticky="W", pady=2)

        def connect_mysql():
            status = connection_sql.connect_to_db(host_entry.get(), db_entry.get(), un_entry.get(), pw_entry.get())
            if status == "Success":
                self.host = host_entry.get()
                self.database = db_entry.get()
                self.username = un_entry.get()
                self.password = pw_entry.get()
                root.destroy()
            else:
                error_label = Label(root, text="Connection Failed", background="grey", padx=5)
                error_label.grid(row=5, column=2, sticky="W", pady=2, padx=2)

        connect = Button(root, text="Connect", command=connect_mysql)
        connect.grid(row=5, column=0, sticky="EW", pady=2, padx=5)

        root.mainloop()

