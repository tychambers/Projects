from tkinter import *
from tkinter import font, ttk, messagebox
from functions import ConnectionSQL
from gui import MySQLConnection

quotes = ConnectionSQL()
my_sql = MySQLConnection()

root = Tk()
root.title("MyQuotes")
root.iconbitmap(r"cubeicon.ico")
root.geometry("510x500")
root.configure(background="grey")

title_label = Label(root, text="Find A Quote: ", font=("Arabic Transparent", 20, "bold"), background="grey",
                    padx=5)
title_label.grid(row=0, column=0, columnspan=3, sticky="NEWS", pady=2)

text_box = Text(root, height=10, width=60)
text_box.grid(row=1, column=0, columnspan=3)


def generate():
    text_box.delete(1.0, END)
    body = quotes.generate_quote()
    quote = body[0]["quote"]
    author = body[0]["author"]
    text_box.insert(END, f'"{quote}" -{author}')


generate = Button(root, text="Generate Quote", command=generate)
generate.grid(row=5, column=0, sticky="EW", pady=2, padx=5)

connect = Button(root, text="Connect to DB", command=my_sql.connect_to_db)
connect.grid(row=5, column=1, sticky="EW", pady=2, padx=5)


def add_quote():
    host = my_sql.host
    database = my_sql.database
    user = my_sql.username
    password = my_sql.password

    quotes.create_table(host, user, password, database)

    author = quotes.author
    quote = quotes.quote

    quotes.add_quote(host, database, user, password, author, quote)


add = Button(root, text="Add Quote to DB", command=add_quote)
add.grid(row=5, column=2, sticky="EW", pady=2, padx=5)

# Adds Treeview
quote_tree = ttk.Treeview(root, columns=('Column 1', 'Column 2'),
                               show='headings')

# Add column headings
quote_tree.heading('Column 1', text='Author Name')
quote_tree.heading('Column 2', text='Quote')


quote_tree.column("Column 1", width=75)
quote_tree.column("Column 2", width=50)

# Pack the widget
quote_tree.grid(row=6, column=0, columnspan=5, rowspan=7, sticky="NEWS", pady=2)

# Treeview Vertical Scrollbar
tree_scroll = ttk.Scrollbar(root, orient="vertical", command=quote_tree.yview)
quote_tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.grid(row=6, column=5, rowspan=7, sticky="NS", pady=2)


def refresh():
    # removes all entries from the treeview
    quote_tree.delete(*quote_tree.get_children())

    host = my_sql.host
    database = my_sql.database
    username = my_sql.username
    password = my_sql.password

    quotes.get_quotes(host, database, username, password)

    quote_list = quotes.quote_list

    # Add data to tree from membership_type table
    for quote in quote_list:
        quote_tree.insert('', 'end', values=(quote[0], quote[1]))


refresh = Button(root, text="View/Refresh Quotes in DB", command=refresh)
refresh.grid(row=13, column=0, sticky="EW", pady=2, padx=5)


def display():
    item = quote_tree.selection()
    quote_blurb = quote_tree.item(item)
    try:
        author = quote_blurb['values'][0]
        quote = quote_blurb['values'][1]

        # delete text in box above
        text_box.delete(1.0, END)

        # insert values into text box
        text_box.insert(END, f'"{quote}" -{author}')

    except IndexError:
        pass


display = Button(root, text="Display Quote Above", command=display)
display.grid(row=13, column=1, sticky="EW", pady=2, padx=5)


def delete():
    host = my_sql.host
    database = my_sql.database
    username = my_sql.username
    password = my_sql.password

    item = quote_tree.selection()
    quote_blurb = quote_tree.item(item)

    try:
        author = quote_blurb['values'][0]
        quote = quote_blurb['values'][1]

        quotes.delete(host, database, username, password, author, quote)

        current_item = quote_tree.focus()
        quote_tree.delete(current_item)

    except IndexError:
        pass


display = Button(root, text="Delete Quote From DB", command=delete)
display.grid(row=13, column=2, sticky="EW", pady=2, padx=5)

root.mainloop()
