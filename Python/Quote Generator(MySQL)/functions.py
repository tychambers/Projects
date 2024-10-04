import mysql.connector
import requests


class ConnectionSQL:
    def __init__(self):
        self.author = ""
        self.quote = ""
        self.quote_list = []

    def connect_to_db(self, host, database, user, password):

        try:
            db = mysql.connector.connect(
                host=f"{host}",
                user=f"{user}",
                passwd=f"{password}",
                database=f"{database}"
            )

            return "Success"

        except:
            return "Failed"

    def create_table(self, host, user, password, database):
        db = mysql.connector.connect(
            host=f"{host}",
            user=f"{user}",
            passwd=f"{password}"
        )

        my_cursor = db.cursor()

        my_cursor.execute(f"USE {database}")
        my_cursor.execute("SHOW TABLES")

        quotes_table = my_cursor.fetchall()

        if not quotes_table:
            query = '''CREATE TABLE Quotes (
                           Author varchar(255),
                           Quote varchar(2000));'''

            my_cursor.execute(query)
            db.commit()
            my_cursor.close()
            db.close()

        else:
            my_cursor.close()
            db.close()

    def add_quote(self, host, database, user, password, author, quote):
        db = mysql.connector.connect(
            host=f"{host}",
            user=f"{user}",
            passwd=f"{password}",
            database=f"{database}"
        )

        my_cursor = db.cursor()

        query = f'''INSERT INTO Quotes (Author, Quote)
        VALUES ("{author}", "{quote}");'''

        my_cursor.execute(query)

        db.commit()
        my_cursor.close()
        db.close()

    def generate_quote(self):

        api_key = "kwKyNgkBqSOU76K0t1qt6g==nNlcsINDYcB5omKm"

        category = 'inspirational'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})
        if response.status_code == requests.codes.ok:
            body = response.json()
            self.quote = body[0]["quote"]
            self.author = body[0]["author"]
            return response.json()
        else:
            return "Error:", response.status_code, response.text

    def get_quotes(self, host, database, user, password):

        db = mysql.connector.connect(
            host=f"{host}",
            user=f"{user}",
            passwd=f"{password}",
            database=f"{database}"
        )

        my_cursor = db.cursor()

        my_cursor.execute("SELECT * FROM Quotes")
        quote_list = my_cursor.fetchall()
        self.quote_list = quote_list
        my_cursor.close()
        db.close()

    def delete(self, host, database, user, password, author, quote):

        db = mysql.connector.connect(
            host=f"{host}",
            user=f"{user}",
            passwd=f"{password}",
            database=f"{database}"
        )

        my_cursor = db.cursor()

        query = f'''DELETE FROM Quotes
        WHERE Author='{author}'
        AND Quote='{quote}';'''

        my_cursor.execute(query)

        db.commit()
        my_cursor.close()
        db.close()