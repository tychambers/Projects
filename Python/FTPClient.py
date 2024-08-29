from tkinter import *
from tkinter import filedialog
from ftplib import FTP

root = Tk()
root.title("FTPClient")
#function to look for files and select a file to upload
button_press = 0


def look_for_file():
    global filename_entry
    global button_press
    button_press = 1
    root.filename = filedialog.askopenfile(initialdir="C:/", title="Select A File", filetypes=[("All Files", "*.*")])
    #returns the file name to print, etc
    file_name = root.filename.name
    entry_text = StringVar()
    filename_entry = Entry(root, textvariable=entry_text)
    new_text = file_name
    entry_text.set(new_text)
    filename_entry.grid(row=1, column=1)





## Connection string boxes ##


#host address#
host_address_label = Label(root, text="Host Address:")
host_address_label.grid(row=0, column=0)
host_address_entry = Entry(root)
host_address_entry.grid(row=0, column=1)
#username#
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=2)
username_entry = Entry(root)
username_entry.grid(row=0, column=3)
#password#
password_label = Label(root, text="Password:")
password_label.grid(row=0, column=4)
password_entry = Entry(root)
password_entry.grid(row=0, column=5)
#file name#
filename_label = Label(root, text="File Name:")
filename_label.grid(row=1, column=0)
filename_entry = Entry(root)
filename_entry.grid(row=1, column=1)

#function for uploading files, has error handling for bad path allows both '\' and '/' paths


def upload_file():
    global button_press
    host_address = host_address_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    filename = filename_entry.get()


    with FTP(host_address) as ftp:
        ftp.login(user=username, passwd=password)
        print(ftp.getwelcome())
        print(filename)
        if button_press == 1:
            filename_parse = filename.split("/")
            fp_count = len(filename_parse) - 1
            print(filename_parse[fp_count])
            button_press = 0
        else:
            filename_parse = filename.split("\\")
            fp_count = len(filename_parse) - 1
            print(filename_parse[fp_count])
        try:
            with open(f"{filename}", "rb") as f:
                ftp.storbinary('STOR ' + filename_parse[fp_count], f)
        except:
            filename_parse = filename.split("/")
            fp_count = len(filename_parse) - 1
            print(filename_parse[fp_count])

            with open(f"{filename}", "rb") as f:
                ftp.storbinary('STOR ' + filename_parse[fp_count], f)


        ftp.quit()


## Buttons ##

#Choose File Button#
choose_file_button = Button(root, text="Choose File", command=look_for_file)
choose_file_button.grid(row=1, column=2)

#Upload Button#
upload_button = Button(root, text="Upload", command=upload_file)
upload_button.grid(row=0, column=6)


root.mainloop()

