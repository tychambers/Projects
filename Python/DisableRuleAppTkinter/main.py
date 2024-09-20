from functions import EFTServer
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Disable Rule")
root.iconbitmap(r"cubeicon.ico")
root.geometry("380x450")
root.configure(background="grey")

root.grid()

title_label = Label(root, text="Disable Rule Tool", font=("Brock Script", 20, "bold"), background="grey",
                    padx=5)
title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

host_label = Label(root, text="Host Address: ", background="grey", padx=5)
host_label.grid(row=2, column=0, sticky="W", pady=2, padx=2)
host_entry = Entry(root, width=35)
host_entry.insert(0, "localhost")
host_entry.grid(row=2, column=1, columnspan=2, sticky="NEWS", pady=2)

port_label = Label(root, text="Port: ", background="grey", padx=5)
port_label.grid(row=3, column=0, sticky="W", pady=2, padx=2)
port_entry = Entry(root, width=35)
port_entry.insert(0, "1100")
port_entry.grid(row=3, column=1, columnspan=2, sticky="NEWS", pady=2)

admin_label = Label(root, text="Admin Username: ", background="grey", padx=5)
admin_label.grid(row=4, column=0, sticky="W", pady=2, padx=2)
admin_entry = Entry(root, width=35)
admin_entry.grid(row=4, column=1, columnspan=2, sticky="NEWS", pady=2)

password_label = Label(root, text="Password: ", background="grey", padx=5)
password_label.grid(row=5, column=0, sticky="W", pady=2, padx=2)
password_entry = Entry(root, show="*", width=35)
password_entry.grid(row=5, column=1, columnspan=2, sticky="NEWS", pady=2)


def login():
    try:
        eft = EFTServer(eft_server=host_entry.get(), eft_port=port_entry.get(), eft_user=admin_entry.get(),
                        eft_password=password_entry.get())
        eft.get_rules()
        rule_list = eft.rule_list

        login_success_label = Label(root, text="Login Success", background="grey", padx=5)
        login_success_label.grid(row=7, column=1, sticky="W", pady=2, padx=2)

        clicked = StringVar()
        clicked.set("Select Rule")
        log_entry_drop = OptionMenu(root, clicked, *rule_list)
        log_entry_drop.grid(row=7, column=1, columnspan=2, sticky="NEWS", pady=2)


        def disable_rule():
            eft.disable_rule(clicked.get())

        disable_rule_button = Button(root, text="Disable Rule", command=disable_rule)
        disable_rule_button.grid(row=8, column=1, sticky="NEWS", pady=2)

        def enable_rule():
            eft.enable_rule(clicked.get())

        enable_rule_button = Button(root, text="Enable Rule", command=enable_rule)
        enable_rule_button.grid(row=8, column=2, sticky="NEWS", pady=2)

    except:
        login_failed_label = Label(root, text="Login Failed", background="grey", padx=5)
        login_failed_label.grid(row=7, column=1, sticky="W", pady=2, padx=2)


login_button = Button(root, text="Login", command=login)
login_button.grid(row=6, column=1, sticky="NEWS", pady=2)

root.mainloop()
