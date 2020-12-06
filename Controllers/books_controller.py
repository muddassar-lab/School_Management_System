from Models import books_database
from tabulate import tabulate


class books_controller:
    def __init__(self, connection):
        self.books_database = books_database.books_database(connection=connection)

    def add_book(self):
        book_name = input("Enter Book Name : ")
        book_isbn = input("Enter Book ISBN : ")
        book_author = input("Enter Book Author Name : ")
        book_edition = input("Enter Book Edition : ")
        book_copies = input("Enter Book Copies : ")
        check_if_empty = self._check_empty(book_name, book_isbn, book_author, book_edition, book_copies)
        if check_if_empty is True:
            print("All fields should be filled.")
        elif check_if_empty is False:
            check_isbn = self.books_database.check_book(book_isbn)
            if check_isbn is True:
                print(f"Book with this ISBN : {book_isbn} already exists. ")
            elif check_isbn is False:
                self.books_database.add_book(book_name, book_isbn, book_author, book_edition, book_copies)

    def list_books(self):
        data = self.books_database.list_books()
        if data is not False:
            print(tabulate(data, headers=["id", "Name", "ISBN", "Author", "Edition", "Copies"]))
        else:
            print("No book record found.")

    def _check_empty(self, *args):
        for argument in args:
            if argument == "":
                return True
        return False

    def search_book_name(self):
        book_name = input("Enter Book Name : ")
        check_if_empty = self._check_empty(book_name)
        if check_if_empty is True:
            print("Name field is empty")
        elif check_if_empty is False:
            data = self.books_database.search_book_name(book_name)
            if data:
                print(tabulate(data, headers=["id", "Name", "ISBN", "Author", "Edition", "Copies"]))
            else:
                print(f"No books with this name : {book_name} found.")

    def search_book_author(self):
        author_name = input("Enter Author Name :")
        check_if_empty = self._check_empty(author_name)
        if check_if_empty is True:
            print("Author Name is Empty.")
        elif check_if_empty is False:
            data = self.books_database.search_book_author(author_name)
            if data:
                print(tabulate(data, headers=["id", "Name", "ISBN", "Author", "Edition", "Copies"]))
            else:
                print(f"No books with this author name : {author_name} found.")

    def search_book_isbn(self):
        isbn = input("Enter ISBN : ")
        check_if_empty = self._check_empty(isbn)
        if check_if_empty is True:
            print("ISBN field is empty")
        elif check_if_empty is False:
            data = self.books_database.search_book_isbn(isbn)
            if data:
                print(f'Book Id : {data[0]}')
                print(f'Book Name : {data[1]}')
                print(f'Book author : {data[2]}')
                print(f'Book isbn : {data[3]}')
                print(f'Book edition : {data[4]}')
                print(f'Book copies : {data[5]}')
            else:
                print(f"No book with this isbn : {isbn} found.")

    def search_book_edition(self):
        book_edition = input("Enter Book Edition : ")
        check_if_empty = self._check_empty(book_edition)
        if check_if_empty is True:
            print("Book edition field is empty.")
        elif check_if_empty is False:
            data = self.books_database.search_book_edition(book_edition)
            if data:
                print(tabulate(data, headers=["id", "Name", "ISBN", "Author", "Edition", "Copies"]))
            else:
                print(f"No books with this edition : {book_edition} found")

    def delete_book(self):
        book_isbn = input("Enter Book ISBN : ")
        check_if_empty = self._check_empty(book_isbn)
        if check_if_empty is True:
            print("Book ISBN field is empty.")
        elif check_if_empty is False:
            self.books_database.delete_book(isbn=book_isbn)

    def update_book(self):
        book_isbn = input("Enter Book ISBN : ")
        check_isbn_empty = self._check_empty(book_isbn)
        if check_isbn_empty is True:
            print("Book ISBN field is empty.")
        elif check_isbn_empty is False:
            check_isbn = self.books_database.check_book(book_isbn)
            if check_isbn is True:
                book_name = input("Enter Book Name : ")
                book_author = input("Enter Book Author Name : ")
                book_edition = input("Enter Book Edition : ")
                book_copies = input("Enter Book Copies : ")
                check_if_empty = self._check_empty(book_name, book_author, book_edition, book_copies)
                if check_if_empty is True:
                    print("All fields should be filled.")
                elif check_if_empty is False:
                    self.books_database.update_book(book_name, book_author, book_isbn, book_edition, book_copies)
            elif check_isbn is False:
                print(f"No book with this isbn : {book_isbn} found.")
