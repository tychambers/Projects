import sqlite3


class MemberDB:
    def __init__(self):
        self.membership_data = []
        self.membership_type_list = []
        self.members = []
        self.memberships = []

    def create_db(self):

        # Connecting to sqlite
        # connection object
        connection_obj = sqlite3.connect('MemberTracker.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # test if table exists
        get_table_names_query = '''SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;'''

        table_list = cursor_obj.execute(get_table_names_query)
        tables = table_list.fetchall()

        if not tables:
            # Creating table

            # Drops table if needed
            # cursor_obj.execute("DROP TABLE IF EXISTS Membership_Type")

            table = """ CREATE TABLE Membership_Type (
                                Membership_Type CHAR(25) NOT NULL,
                                Monthly_Price REAL(25) NOT NULL,
                                Perks TEXT(255)
                            ); """

            insert_into_table = ''' INSERT INTO Membership_Type (Membership_Type,Monthly_Price,Perks)
                                  VALUES(?,?,?) '''

            premium = ["Premium", 50.00, "Unlimited Access, Sauna, Tennis Courts"]
            professional = ["Professional", 35.00, "Unlimited Access, Sauna"]
            basic = ["Basic", 25.00, "Unlimited Access"]

            cursor_obj.execute(table)
            cursor_obj.execute(insert_into_table, premium)
            cursor_obj.execute(insert_into_table, professional)
            cursor_obj.execute(insert_into_table, basic)

            # Add member table

            # drops existing table

            # cursor_obj.execute("DROP TABLE IF EXISTS Members")

            member_table = """ CREATE TABLE Members (
                                First_Name CHAR(25) NOT NULL,
                                Last_Name CHAR(25) NOT NULL,
                                Email VARCHAR(255) NOT NULL,
                                Membership_Type CHAR(25) NOT NULL,
                                FOREIGN KEY(Membership_Type) REFERENCES Membership_Type(Membership_Type)
                            ); """

            cursor_obj.execute(member_table)

        # Pull all membership type information from DB

        select_member_type = ''' SELECT * FROM Membership_Type '''

        cursor_obj.execute(select_member_type)
        data = cursor_obj.fetchall()
        self.membership_data = data

        select_member_type_field = ''' SELECT Membership_Type FROM Membership_Type '''

        cursor_obj.execute(select_member_type_field)
        member_data = cursor_obj.fetchall()
        self.membership_type_list = member_data
        # Commit all queries

        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()

    def add_member(self, first_name, last_name, email, membership_type):

        connection_obj = sqlite3.connect('MemberTracker.db')

        cursor_obj = connection_obj.cursor()

        # parse the correct value for membership type
        m2 = membership_type.strip("'),")
        m3 = m2.strip("('")

        # enter entry into table
        table_entry_list = [first_name, last_name, email, m3]

        insert_into_table = ''' INSERT INTO Members (First_Name,Last_Name,Email,Membership_Type)
                              VALUES(?,?,?,?) '''

        cursor_obj.execute(insert_into_table, table_entry_list)

        connection_obj.commit()

        cursor_obj.close()
        connection_obj.close()

    def display_members(self, membership_type):

        connection_obj = sqlite3.connect('MemberTracker.db')

        cursor_obj = connection_obj.cursor()

        query = f'''SELECT * 
                FROM Members 
                WHERE ( Membership_Type = '{membership_type}' )'''

        get_info = cursor_obj.execute(query)
        tables = get_info.fetchall()
        self.members = tables

    def delete_user(self, first_name, last_name, email):

        connection_obj = sqlite3.connect('MemberTracker.db')
        cursor_obj = connection_obj.cursor()

        query = f'''DELETE 
                FROM Members 
                WHERE ( First_Name = '{first_name}' )
                AND ( Last_Name = '{last_name}' )
                AND ( Email = '{email}' )'''

        cursor_obj.execute(query)
        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()

    def add_membership(self, membership_type, monthly_payment, perks):
        connection_obj = sqlite3.connect('MemberTracker.db')
        cursor_obj = connection_obj.cursor()

        insert_into_table = ''' INSERT INTO Membership_Type (Membership_Type,Monthly_Price,Perks)
                                          VALUES(?,?,?) '''

        entry = [membership_type, monthly_payment, perks]

        cursor_obj.execute(insert_into_table, entry)
        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()

    def remove_membership(self, membership_type):

        connection_obj = sqlite3.connect('MemberTracker.db')
        cursor_obj = connection_obj.cursor()

        query1 = f'''DELETE 
                FROM Members 
                WHERE ( Membership_Type = '{membership_type}' )'''

        cursor_obj.execute(query1)
        connection_obj.commit()

        query2 = f'''DELETE 
                    FROM Membership_Type 
                    WHERE ( Membership_Type = '{membership_type}' )'''

        cursor_obj.execute(query2)
        connection_obj.commit()
        cursor_obj.close()
        connection_obj.close()

    def refresh_membership_list(self):
        connection_obj = sqlite3.connect('MemberTracker.db')

        cursor_obj = connection_obj.cursor()

        query = f'''SELECT * 
                FROM Membership_Type'''

        get_info = cursor_obj.execute(query)
        tables = get_info.fetchall()
        self.memberships = tables
