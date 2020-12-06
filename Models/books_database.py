class books_database:
    def __init__(self, connection):
        self.connection = connection

    def check_book(self, isbn):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn=?", (isbn,))
        data = cursor.fetchone()
        if data:
            return True
        else:
            return False

    def add_book(self, book_name, book_isbn, book_author, book_edition, book_copies):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO books(name,isbn,author,edition,copies) VALUES(?,?,?,?,?)",
                       (book_name, book_isbn, book_author, book_edition, book_copies))
        self.connection.commit()

    def list_books(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books")
        data = cursor.fetchall()
        return data

    def search_book_name(self, bookname):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE name=?", (bookname,))
        data = cursor.fetchall()
        return data

    def search_book_author(self, authorname):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE author=?", (authorname,))
        data = cursor.fetchall()
        return data

    def search_book_isbn(self, isbn):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE isbn=?", (isbn,))
        data = cursor.fetchone()
        return data

    def search_book_edition(self, edition):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books WHERE edition=?", (edition,))
        data = cursor.fetchall()
        return data

    def delete_book(self, isbn):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM books WHERE isbn=?", (isbn,))
        self.connection.commit()

    def update_book(self, name, author, isbn, edition, copies):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE books SET name=?,author=?,edition=?,copies=? WHERE isbn=?",
                       (name, author, edition, copies, isbn))
        self.connection.commit()
