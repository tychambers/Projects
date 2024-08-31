from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Appender Generator")
root.iconbitmap(r"cubeicon.ico")
root.geometry("380x450")
root.configure(background="grey")

my_notebook = ttk.Notebook(root)
my_notebook.grid()

my_frame1 = Frame(my_notebook, bg="grey", highlightcolor="grey", highlightbackground="grey")
my_frame2 = Frame(my_notebook, width=1000, height=1000, bg="grey")
my_frame3 = Frame(my_notebook, width=1000, height=1000, bg="grey")

my_frame1.grid()
my_frame2.grid()
my_frame3.grid()

my_notebook.add(my_frame1, text="General")
my_notebook.add(my_frame2, text="FM Rule")
my_notebook.add(my_frame3, text="Keyword")

title_label = Label(my_frame1, text="Appender Generator", font=("Brock Script", 20, "bold"), background="grey",
                    padx=5)
title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

name_label = Label(my_frame1, text="Input the Appender Name: ", background="grey", padx=5)
name_label.grid(row=2, column=0, sticky="W", pady=2, padx=2)
name_entry = Entry(my_frame1, width=35)
name_entry.grid(row=2, column=1, columnspan=2, sticky="NEWS", pady=2)

log_entry_label = Label(my_frame1, text="Select Logging.cfg entries: ", background="grey", padx=5)
log_entry_label.grid(row=3, column=0, sticky="W", pady=2)

entry_list = []
logging_entry_label = Label(my_frame1, text="Entries: None", background="grey")
logging_entry_label.grid(row=6, column=0, sticky="W", pady=2)

def add_entry():
    global entry_list
    global logging_entry_label
    new_entry = clicked.get() + "=" + clicked2.get()
    entry_list.append(new_entry)
    logging_entry_label.grid_remove()
    text = "Entries: "
    for entry in entry_list:
        text += entry + ", "

    text = text[:-2]

    logging_entry_label = Label(my_frame1, text=text, background="grey")
    logging_entry_label.grid(row=6, column=0, columnspan=3, sticky="W")

def remove_entry():
    global logging_entry_label
    logging_entry_label.grid_forget()
    last_item = len(entry_list) - 1
    entry_list.pop(last_item)
    if last_item > 0:
        text = "Entries: "
        for entry in entry_list:
            text += entry + ", "

        text = text[:-2]
        logging_entry_label = Label(my_frame1, text=text, background="grey")
        logging_entry_label.grid(row=6, column=0, sticky="W")
    else:
        logging_entry_label = Label(my_frame1, text="Entries: None", background="grey")
        logging_entry_label.grid(row=6, column=0, sticky="W")


##Log Entries
clicked = StringVar()
clicked.set("Select an entry")
log_entry_drop = OptionMenu(my_frame1, clicked, "Administrator", "Administrator.Permissions", "AdminSupport",
                            "AdvancedProperties", "ARM", "ARM.Queue", "AS2", "AUD.Read", "AUD.Write", "AuthManager",
                            "AWE", "Backup", "CFG.Read", "CFG.Write", "ClientManager", "ClientTransfers", "CmdAccess",
                            "Common", "DMZSupport", "Events", "FileSystem", "FTP", "HTTP", "IPAccess", "PathManager",
                            "PGP.Adapter", "Registration", "Reporting", "Reports", "Server.Startup", "Server.Stop",
                            "Service", "SFTP", "SMTP", "SSL", "Timer", "Cluster", "Workspaces", "SAMLSSO", "Cloud",
                            "Admin.API", "Remote.Agent", "CAPTCHA", "EncryptedFolders", "User.API", "SecretsModule",
                            "SMS", "UploadQuota")
log_entry_drop.grid(row=3, column=1, columnspan=2, sticky="NEWS", pady=2)
#Logging level
clicked2 = StringVar()
clicked2.set("Select Logging Level")
log_level_drop = OptionMenu(my_frame1, clicked2, "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL", "OFF")
log_level_drop.grid(row=4, column=1, columnspan=2, sticky="NEWS", pady=2)

add_entry_button = Button(my_frame1, text="Add Entry", command=add_entry)
add_entry_button.grid(row=5, column=1, sticky="NEWS", pady=2)

remove_entry_button = Button(my_frame1, text="Remove Entry", command=remove_entry)
remove_entry_button.grid(row=5, column=2, sticky="NEWS", pady=2)

#added_entry_label = Label(root, text="Added Entries:", background="grey")
#added_entry_label.grid(row=6, column=0, sticky="W", pady=2)

#Generate the appender#

def create_appender():
    appender_name = name_entry.get()
    pre_str = "log4cplus.appender." + appender_name.lower()

    l2 = f'{pre_str}=log4cplus::RollingFileAppender'
    l3 = f'{pre_str}.File=${{AppDataPath}}\\EFT-{appender_name.lower()}.log'
    l4 = f'{pre_str}.MaxFileSize=20MB'
    l5 = f'{pre_str}.MaxBackupIndex=5'
    l6 = f'{pre_str}.layout=log4cplus::TTCCLayout'
    l7 = f'{pre_str}.layout.DateFormat=%m-%d-%y %H:%M:%S,%q'
    l8 = ''
    l9 = ''

    while entry_list:
        ap = entry_list.pop()
        ap1 = ap.split("=")[0]
        ap2 = ap.split("=")[1]
        l8 += f'log4cplus.additivity.{ap1}=false\n'
        l9 += f'log4cplus.logger.{ap1}={ap2}, {appender_name.lower()}\n'

    text_body = [l2, l3, l4, l5, l6, l7, l8, l9]

    text_box = Text(my_frame1, width=40, height=12)
    for line in text_body:
        text_box.insert(END, f"{line}\n")

    text_box.grid(row=8, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)
    global logging_entry_label
    logging_entry_label.grid_remove()
    logging_entry_label = Label(my_frame1, text="Entries: None", background="grey")
    logging_entry_label.grid(row=6, column=0, sticky="W")

text_box = Text(my_frame1, width=40, height=12)
text_box.grid(row=8, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)
create_appender_button = Button(my_frame1, text="Create Appender", command=create_appender)
create_appender_button.grid(row=7, column=1, columnspan=2, sticky="NEWS", pady=2)

###FM Appender TAB###
#####################

title_label = Label(my_frame2, text="FM Rule Appender", font=("Brock Script", 20, "bold"), background="grey",
                    padx=5)
title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

name_label2 = Label(my_frame2, text="Input the Appender Name: ", background="grey", padx=5)
name_label2.grid(row=2, column=0, sticky="W", pady=2)
name_entry2 = Entry(my_frame2, width=35)
name_entry2.grid(row=2, column=1, columnspan=2, sticky="NEWS", pady=2)

site_entry_label = Label(my_frame2, text="Input Site Name: ", background="grey", padx=5)
site_entry_label.grid(row=3, column=0, sticky="W", pady=2)
site_entry = Entry(my_frame2, width=35)
site_entry.grid(row=3, column=1, columnspan=2, sticky="NEWS", pady=2)

rule_entry_label = Label(my_frame2, text="Input Rule Name: ", background="grey", padx=5)
rule_entry_label.grid(row=4, column=0, sticky="W", pady=2)
rule_entry = Entry(my_frame2, width=35)
rule_entry.grid(row=4, column=1, columnspan=2, sticky="NEWS", pady=2)

logging_entry_label2 = Label(my_frame2, text="Entries: ", background="grey")
logging_entry_label2.grid(row=6, column=0, columnspan=3, sticky="W")

rule_list = []
def add_button():
    global rule_list
    global logging_entry_label2
    site_name = site_entry.get()
    rule_name = rule_entry.get()
    rule = site_name + "." + rule_name
    rule_list.append(rule)

    text = "Entries: "
    for entry in rule_list:
        text += entry + ","

    text = text[:-2]

    logging_entry_label2.grid_forget()
    logging_entry_label2 = Label(my_frame2, text=text, background="grey")
    logging_entry_label2.grid(row=6, column=0, columnspan=3, sticky="W")


add_button2 = Button(my_frame2, text="Add Entry", command=add_button)
add_button2.grid(row=5, column=1, sticky="NEWS", pady=2)

def remove_button():
    global logging_entry_label2
    logging_entry_label2.grid_forget()
    last_item = len(rule_list) - 1
    rule_list.pop(last_item)
    if last_item > 0:
        text = "Entries: "
        for entry in rule_list:
            text += entry + ", "

        text = text[:-2]
        logging_entry_label2 = Label(my_frame2, text=text, background="grey")
        logging_entry_label2.grid(row=6, column=0, sticky="W")
    else:
        logging_entry_label2 = Label(my_frame2, text="Entries: None", background="grey")
        logging_entry_label2.grid(row=6, column=0, sticky="W")


remove_button2 = Button(my_frame2, text="Remove Entry", command=remove_button)
remove_button2.grid(row=5, column=2, sticky="NEWS", pady=2)

def create_fm_appender():
    appender_name = name_entry2.get()
    pre_str = "log4cplus.appender." + appender_name.lower()

    l2 = f'{pre_str}=log4cplus::RollingFileAppender'
    l3 = f'{pre_str}.File=${{AppDataPath}}\\EFT-{appender_name.lower()}.log'
    l4 = f'{pre_str}.MaxFileSize=20MB'
    l5 = f'{pre_str}.MaxBackupIndex=5'
    l6 = f'{pre_str}.layout=log4cplus::TTCCLayout'
    l7 = f'{pre_str}.layout.DateFormat=%m-%d-%y %H:%M:%S,%q'
    l8 = ''
    l9 = ''

    while rule_list:
        ap = rule_list.pop()
        l8 += f'log4cplus.additivity.{ap}=false\n'
        l9 += f'log4cplus.logger.Events.FolderMonitor.{ap}=TRACE, {appender_name.lower()}\n'

    text_body = [l2, l3, l4, l5, l6, l7, l8, l9]

    text_box = Text(my_frame2, width=40, height=12)
    for line in text_body:
        text_box.insert(END, f"{line}\n")

    text_box.grid(row=8, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)
    global logging_entry_label2
    logging_entry_label2.grid_remove()
    logging_entry_label2 = Label(my_frame2, text="Entries: None", background="grey")
    logging_entry_label2.grid(row=6, column=0, sticky="W")

text_box = Text(my_frame2, width=40, height=13)
text_box.grid(row=8, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)

create_fm_appender_button = Button(my_frame2, text="Create Appender", command=create_fm_appender)
create_fm_appender_button.grid(row=7, column=1, columnspan=2, sticky="NEWS", pady=2)

##KEY WORD TAB##
################

title_label3 = Label(my_frame3, text="Keyword Appender", font=("Brock Script", 20, "bold"), background="grey", padx=5)
title_label3.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

name_label2 = Label(my_frame3, text="Input the Appender Name: ", background="grey", padx=5)
name_label2.grid(row=2, column=0, sticky="W", pady=2)
name_entry2 = Entry(my_frame3, width=35)
name_entry2.grid(row=2, column=1, columnspan=2, sticky="NEWS", pady=2)

log_entry_label2 = Label(my_frame3, text="Select Logging.cfg entries: ", background="grey", padx=5)
log_entry_label2.grid(row=3, column=0, sticky="W", pady=2)

logging_entry_label2 = Label(my_frame3, text="Entries: None", background="grey")
logging_entry_label2.grid(row=6, column=0, sticky="W", pady=2)

##Log Entries


clicked3 = StringVar()
clicked3.set("Select an entry")
log_entry_drop2 = OptionMenu(my_frame3, clicked3, "Administrator", "Administrator.Permissions", "AdminSupport",
                            "AdvancedProperties", "ARM", "ARM.Queue", "AS2", "AUD.Read", "AUD.Write", "AuthManager",
                            "AWE", "Backup", "CFG.Read", "CFG.Write", "ClientManager", "ClientTransfers", "CmdAccess",
                            "Common", "DMZSupport", "Events", "FileSystem", "FTP", "HTTP", "IPAccess", "PathManager",
                            "PGP.Adapter", "Registration", "Reporting", "Reports", "Server.Startup", "Server.Stop",
                            "Service", "SFTP", "SMTP", "SSL", "Timer", "Cluster", "Workspaces", "SAMLSSO", "Cloud",
                            "Admin.API", "Remote.Agent", "CAPTCHA", "EncryptedFolders", "User.API", "SecretsModule",
                            "SMS", "UploadQuota")
log_entry_drop2.grid(row=3, column=1, columnspan=2, sticky="NEWS", pady=2)
#Logging level
clicked4 = StringVar()
clicked4.set("Select Logging Level")
log_level_drop2 = OptionMenu(my_frame3, clicked4, "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL", "OFF")
log_level_drop2.grid(row=4, column=1, columnspan=2, sticky="NEWS", pady=2)

entry_list2 = []


def add_entry2():
    global entry_list2
    global logging_entry_label2
    new_entry = clicked3.get() + "=" + clicked4.get()
    entry_list2.append(new_entry)
    logging_entry_label2.grid_remove()
    text = "Entries: "
    for entry in entry_list2:
        text += entry + ", "

    text = text[:-2]

    logging_entry_label2 = Label(my_frame3, text=text, background="grey")
    logging_entry_label2.grid(row=6, column=0, columnspan=3, sticky="W")


add_entry_button2 = Button(my_frame3, text="Add Entry", command=add_entry2)
add_entry_button2.grid(row=5, column=1, sticky="NEWS", pady=2)


def remove_entry2():
    global logging_entry_label2
    global entry_list2
    logging_entry_label2.grid_forget()
    last_item = len(entry_list2) - 1
    entry_list2.pop(last_item)
    if last_item > 0:
        text = "Entries: "
        for entry in entry_list2:
            text += entry + ", "

        text = text[:-2]
        logging_entry_label2 = Label(my_frame3, text=text, background="grey", pady=2)
        logging_entry_label2.grid(row=6, column=0, sticky="W")
    else:
        logging_entry_label2 = Label(my_frame3, text="Entries: None", background="grey", pady=2)
        logging_entry_label2.grid(row=6, column=0, sticky="W", pady=2)


remove_entry_button2 = Button(my_frame3, text="Remove Entry", command=remove_entry2)
remove_entry_button2.grid(row=5, column=2, sticky="NEWS", pady=2)

filter_entry = Entry(my_frame3, width=35)
filter_entry.grid(row=7, column=1, columnspan=2, sticky="NEWS", pady=2)

filter_label = Label(my_frame3, text="Enter Filter: ", background="grey", padx=2)
filter_label.grid(row=7, column=0, sticky="W", pady=2)

filter_entry_label = Label(my_frame3, text="Keyword Filters: None", background="grey", pady=2)
filter_entry_label.grid(row=9, column=0, columnspan=3, pady=2, sticky="W")

filter_list = []


def add_filter():
    global filter_list
    global filter_entry_label
    filter_ = filter_entry.get()
    if len(filter_) == 0:
        filter_entry_label.grid_remove()
        filter_entry_label = Label(my_frame3, text="Keyword Filters: None", background="grey", pady=2)
        filter_entry_label.grid(row=9, column=0, columnspan=3, sticky="W", pady=2)
    else:
        filter_list.append(filter_)

        text = "Keyword Filters: "
        for f in filter_list:
            text += f + ", "

        text = text[:-2]
        filter_entry_label.grid_remove()
        filter_entry_label = Label(my_frame3, text=text, background="grey", pady=2)
        filter_entry_label.grid(row=9, column=0, columnspan=3, sticky="W", pady=2)


def remove_filter():
    global filter_list
    global filter_entry_label
    filter_entry_label.grid_remove()
    last_item = len(filter_list) - 1
    filter_list.pop(last_item)
    if last_item > 0:
        text = "Keyword Filters: "
        for entry in filter_list:
            text += entry + ", "

        text = text[:-2]
        filter_entry_label = Label(my_frame3, text=text, background="grey", pady=2)
        filter_entry_label.grid(row=9, column=0, sticky="W", pady=2)
    else:
        filter_entry_label = Label(my_frame3, text="Keyword Filters: None", background="grey", pady=2)
        filter_entry_label.grid(row=9, column=0, sticky="W", pady=2)


add_filter_button = Button(my_frame3, text="Add Filter: ", padx=5, command=add_filter)
add_filter_button.grid(row=8, column=1, sticky="NEWS", pady=2)

rem_filter_button = Button(my_frame3, text="Remove Filter: ", padx=5, command=remove_filter)
rem_filter_button.grid(row=8, column=2, sticky="NEWS", pady=2)


def create_appender2():
    appender_name = name_entry2.get()
    pre_str = "log4cplus.appender." + appender_name.lower()

    lm2 = ''
    lm1 = ''
    l0 = ''
    l1 = ''
    l2 = f'{pre_str}=log4cplus::RollingFileAppender'
    l3 = f'{pre_str}.File=${{AppDataPath}}\\EFT-{appender_name.lower()}.log'
    l4 = f'{pre_str}.MaxFileSize=20MB'
    l5 = f'{pre_str}.MaxBackupIndex=5'
    l6 = f'{pre_str}.layout=log4cplus::TTCCLayout'
    l7 = f'{pre_str}.layout.DateFormat=%m-%d-%y %H:%M:%S,%q'
    l8 = ''
    l9 = ''

    while entry_list2:
        ap = entry_list2.pop()
        ap1 = ap.split("=")[0]
        ap2 = ap.split("=")[1]
        l8 += f'log4cplus.additivity.{ap1}=false\n'
        l9 += f'log4cplus.logger.{ap1}={ap2}, {appender_name.lower()}\n'

    number = 1
    while filter_list:
        ax = filter_list.pop()
        lm2 += f'log4cplus.appender.{appender_name.lower()}.filters.{number}=log4cplus::spi::StringMatchFilter\n'
        lm1 += f'log4cplus.appender.{appender_name.lower()}.filters.{number}.StringToMatch={ax}\n'
        l0 += f'log4cplus.appender.{appender_name.lower()}.filters.{number}.AcceptOnMatch=true\n'
        number = number + 1

    lm2 = lm2[:-1]
    lm1 = lm1[:-1]
    l0 = l0[:-1]

    l1 += f'log4cplus.appender.{appender_name.lower()}.filters.{number}.log4cplus::spi::DenyAllFilter\n'

    text_body = [lm2, lm1, l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]

    text_box = Text(my_frame3, width=40, height=7)
    for line in text_body:
        text_box.insert(END, f"{line}\n")

    text_box.grid(row=11, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)
    global logging_entry_label2
    logging_entry_label2.grid_remove()
    logging_entry_label2 = Label(my_frame3, text="Entries: None", background="grey")
    logging_entry_label2.grid(row=6, column=0, sticky="W")

text_box = Text(my_frame3, width=40, height=7)
text_box.grid(row=11, column=0, columnspan=3, sticky="NEWS", padx=5, pady=5)

create_appender_button2 = Button(my_frame3, text="Create Appender", command=create_appender2)
create_appender_button2.grid(row=10, column=1, columnspan=2, sticky="NEWS", pady=2)

root.mainloop()