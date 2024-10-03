from tkinter import *
from tkinter import ttk, messagebox
from functions import MemberDB

member_db = MemberDB()
member_db.create_db()
member_data = member_db.membership_data

root = Tk()
root.title("MemberTracker")
root.iconbitmap(r"cubeicon.ico")
root.geometry("950x600")
root.configure(background="grey")

# Title

title_label = Label(root, text="Member Tracker", font=("Brock Script", 20, "bold"), background="grey",
                    padx=5)
title_label.grid(row=0, column=3, columnspan=3, sticky="NEWS", pady=2)

membership_title_label = Label(root, text="Membership Type: ", font=("Brock Script", 16, "bold"), background="grey",
                    padx=5)
membership_title_label.grid(row=1, column=0, columnspan=3, sticky="W", pady=2)

# Adds Treeview
membership_tree = ttk.Treeview(root, columns=('Column 1', 'Column 2', 'Column 3'),
                               show='headings')

# Add column headings
membership_tree.heading('Column 1', text='Membership Type')
membership_tree.heading('Column 2', text='Monthly Price')
membership_tree.heading('Column 3', text='Perks')

membership_tree.column("Column 1", width=75)
membership_tree.column("Column 2", width=50)

# Add data to tree from membership_type table
for membership in member_data:
    membership_tree.insert('', 'end', values=(membership[0], membership[1], membership[2]))

# Pack the widget
membership_tree.grid(row=2, column=0, columnspan=5, rowspan=7, sticky="NEWS", pady=2)

# Treeview Vertical Scrollbar
tree_scroll = ttk.Scrollbar(root, orient="vertical", command=membership_tree.yview)
membership_tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.grid(row=2, column=5, rowspan=7, sticky="NS", pady=2)

# deletes highlighted
# member_listbox.delete(ANCHOR)

# Add member box

membership_title_label = Label(root, text="Add Member: ", font=("Brock Script", 16, "bold"), background="grey",
                    padx=5)
membership_title_label.grid(row=9, column=6, columnspan=3, sticky="W", pady=2)

fn_label = Label(root, text="First Name: ", background="grey", padx=5)
fn_label.grid(row=10, column=6, sticky="W", pady=2, padx=2)
fn_entry = Entry(root, width=20)
fn_entry.insert(0, "Enter Name")
fn_entry.grid(row=10, column=7, columnspan=2, sticky="W", pady=2)

ln_label = Label(root, text="Last Name: ", background="grey", padx=5)
ln_label.grid(row=11, column=6, sticky="W", pady=2, padx=2)
ln_entry = Entry(root, width=20)
ln_entry.insert(0, "Enter Name")
ln_entry.grid(row=11, column=7, columnspan=2, sticky="W", pady=2)

email_label = Label(root, text="Email: ", background="grey", padx=5)
email_label.grid(row=12, column=6, sticky="W", pady=2, padx=2)
email_entry = Entry(root, width=20)
email_entry.insert(0, "Enter Email")
email_entry.grid(row=12, column=7, columnspan=2, sticky="W", pady=2)

# drop down for membership type

member_types = member_db.membership_type_list

mt_clicked = StringVar()
mt_clicked.set("Select Membership")
mt_entry_drop = OptionMenu(root, mt_clicked, *member_types)
mt_entry_drop.grid(row=14, column=6, columnspan=2, sticky="W", pady=2, padx=5)


def add_member_to_group():
    first_name = fn_entry.get()
    last_name = ln_entry.get()
    email = email_entry.get()
    membership_type = mt_clicked.get()

    current_item = membership_tree.focus()
    highlighted_row = membership_tree.item(current_item)
    member_type = highlighted_row["values"][0]
    m_type = f"('{member_type}',)"

    member_db.add_member(first_name, last_name, email, membership_type)

    if membership_type == m_type:
        member_viewer_tree.insert("", "end", text="Item 1", values=(first_name, last_name, email))
    else:
        pass


add_member_button = Button(root, text="Add Member", command=add_member_to_group)
add_member_button.grid(row=15, column=6, sticky="EW", pady=2, padx=5)


def remove_member():
    current_item = member_viewer_tree.focus()
    highlighted_row = member_viewer_tree.item(current_item)
    first_name = highlighted_row["values"][0]
    last_name = highlighted_row["values"][1]
    email = highlighted_row["values"][2]
    member_db.delete_user(first_name, last_name, email)

    member_viewer_tree.delete(current_item)


remove_member_button = Button(root, text="Remove Member", command=remove_member)
remove_member_button.grid(row=15, column=7, sticky="EW", pady=2, padx=5)

# Add Member Title

member_title_label = Label(root, text="Members: ", font=("Brock Script", 16, "bold"), background="grey",
                    padx=5)
member_title_label.grid(row=9, column=0, columnspan=3, sticky="W", pady=2)

# Add the display box for viewing members

member_viewer_tree = ttk.Treeview(root, columns=('Column 1', 'Column 2', 'Column 3'), show='headings')

# Add column headings
member_viewer_tree.heading('Column 1', text='First Name')
member_viewer_tree.heading('Column 2', text='Last Name')
member_viewer_tree.heading('Column 3', text='Email')

member_viewer_tree.grid(row=10, column=0, columnspan=5, rowspan=7, sticky="NEWS", pady=2)

# Treeview Vertical Scrollbar
tree_v_scroll = ttk.Scrollbar(root, orient="vertical", command=member_viewer_tree.yview)
member_viewer_tree.configure(yscrollcommand=tree_v_scroll.set)
tree_v_scroll.grid(row=10, column=5, rowspan=7, sticky="NS", pady=2)

def view_members():
    # remove entries from TreeView

    member_viewer_tree.delete(*member_viewer_tree.get_children())

    # retrieve highlighted membership category from membership table
    try:
        current_item = membership_tree.focus()
        highlighted_row = membership_tree.item(current_item)
        member_type = highlighted_row["values"][0]
        member_db.display_members(member_type)

        members = member_db.members

        for member in members:
            member_viewer_tree.insert('', 'end', values=(member[0], member[1], member[2]))

    except IndexError:
        error_label = Label(root, text="Select Membership Type", background="grey", padx=5)
        error_label.grid(row=9, column=7, sticky="W", pady=2, padx=2)


view_title_label = Label(root, text="View/Edit Membership: ", font=("Brock Script", 16, "bold"), background="grey",
                    padx=5)
view_title_label.grid(row=1, column=6, columnspan=2, sticky="W", pady=2)

view_desc_label = Label(root, text="Highlight membership and click view/refresh for member list", background="grey")
view_desc_label.grid(row=2, column=6, columnspan=2, sticky="W", pady=2)

view_button = Button(root, text="View Members", command=view_members)
view_button.grid(row=3, column=6, sticky="EW", pady=2, padx=5)


def refresh_memberships():
    membership_tree.delete(*membership_tree.get_children())
    member_db.refresh_membership_list()
    memberships = member_db.memberships

    for m in memberships:
        membership_tree.insert('', 'end', values=(m[0], m[1], m[2]))


refresh_button = Button(root, text="Refresh Memberships", command=refresh_memberships)
refresh_button.grid(row=3, column=7, sticky="EW", pady=2, padx=5)

mt_label = Label(root, text="Membership Type: ", background="grey", padx=5)
mt_label.grid(row=4, column=6, sticky="W", pady=2, padx=2)
mt_entry = Entry(root, width=20)
mt_entry.insert(0, "Member Type")
mt_entry.grid(row=4, column=7, columnspan=2, sticky="W", pady=2)

mp_label = Label(root, text="Monthly Price: ", background="grey", padx=5)
mp_label.grid(row=5, column=6, sticky="W", pady=2, padx=2)
mp_entry = Entry(root, width=20)
mp_entry.insert(0, "0.00")
mp_entry.grid(row=5, column=7, columnspan=2, sticky="W", pady=2)

perks_label = Label(root, text="Perks: ", background="grey", padx=5)
perks_label.grid(row=6, column=6, sticky="W", pady=2, padx=2)
perks_entry = Entry(root, width=20)
perks_entry.insert(0, "Full Access, etc")
perks_entry.grid(row=6, column=7, columnspan=2, sticky="W", pady=2)


def add_membership():
    membership_type = mt_entry.get()
    monthly_payment = mp_entry.get()
    perks = perks_entry.get()

    member_db.add_membership(membership_type, monthly_payment, perks)


add_membership_button = Button(root, text="Add Membership", command=add_membership)
add_membership_button.grid(row=7, column=6, sticky="EW", pady=2, padx=5)


def remove_membership():
    current_item = membership_tree.focus()
    highlighted_row = membership_tree.item(current_item)
    membership_type_name = highlighted_row["values"][0]
    member_db.remove_membership(membership_type_name)

    membership_tree.delete(current_item)


def show_dialog():
    answer = messagebox.askyesno("Warning!", "Deleting a membership group will remove all members in the group. Do you"
                                             " want to proceed?")
    if answer:
        remove_membership()
    else:
        pass


remove_membership_button = Button(root, text="Remove Membership", command=show_dialog)
remove_membership_button.grid(row=7, column=7, sticky="EW", pady=2, padx=5)

root.grid()

root.mainloop()