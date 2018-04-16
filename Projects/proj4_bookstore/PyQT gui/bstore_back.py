import sqlite3

class Database:
    """docstring for Database."""
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor=self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, \
        title text, author text, year integer, isbn integer, date_in text, date_out text)")
        self.connection.commit()

    def insert(self,title,author,year,isbn,date_in,date_out):
        self.cursor.execute("INSERT INTO library VALUES (NULL,?,?,?,?,?,?)",(title,author,year,isbn,date_in,date_out))
        self.connection.commit()

    def view(self):
        result = self.connection.execute("SELECT title,author,year,isbn,date_in,date_out FROM library")
        return result

    def search(self,title="",author="",year="",isbn=""):
        result = self.cursor.execute("SELECT * FROM library WHERE title=? OR author=? OR year=? OR isbn=?",
        (title,author,year,isbn))
        return result

    # def search(self,title="",author="",year="",isbn=""):
    #     self.cursor.execute("SELECT * FROM library WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    #     rows=self.cursor.fetchall()
    #     return rows

    def delete(self,isbn):
        self.cursor.execute("DELETE FROM library WHERE isbn=?", (isbn,))
        self.connection.commit()

    # def update(self,id,title,author,year,isbn):
    #     self.cursor.execute("UPDATE library SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    #     self.connection.commit()

    def __del__(self):
        self.connection.close()
