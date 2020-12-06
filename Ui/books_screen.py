def search_book(bookscontroller):
    userinput = input("Press\n"
                      "'SN' to Search Books by Name\n"
                      "'SA' to Search Books by Auhtor Name\n"
                      "'SI' to Search a Book by ISBN\n"
                      "'SE' to Search a Book by Edition\n"
                      "'Q' to return to Mainmenu\n"
                      " : ")
    while userinput != 'Q':
        if userinput == 'SN':
            bookscontroller.search_book_name()
        elif userinput == "SA":
            bookscontroller.search_book_author()
        elif userinput == "SI":
            bookscontroller.search_book_isbn()
        elif userinput == 'SE':
            bookscontroller.search_book_edition()
        else:
            print("Wrong Command")
        userinput = input("Press\n"
                          "'SN' to Search Books by Name\n"
                          "'SA' to Search Books by Auhtor Name\n"
                          "'SI' to Search a Book by ISBN\n"
                          "'SE' to Search a Book by Edition\n"
                          "'Q' to return to Mainmenu\n"
                          " : ")


def Books(bookscontroller):
    userinput = input("Press\n"
                      "'A' to Add a Book\n"
                      "'L' to List all Books\n"
                      "'S' to Search a Book\n"
                      "'D' to Delete a Book\n"
                      "'U' to Update a Book\n"
                      "'Q' to return to Mainmenu\n"
                      " : ")
    while userinput != 'Q':
        if userinput == 'A':
            bookscontroller.add_book()
        elif userinput == "L":
            bookscontroller.list_books()
        elif userinput == "S":
            search_book(bookscontroller)
        elif userinput == 'D':
            bookscontroller.delete_book()
        elif userinput == "U":
            bookscontroller.update_book()
        else:
            print("Wrong Command")
        userinput = input("Press\n"
                          "'A' to Add a Book\n"
                          "'L' to List all Books\n"
                          "'S' to Search a Book\n"
                          "'D' to Delete a Book\n"
                          "'U' to Update a Book\n"
                          "'Q' to return to Mainmenu\n"
                          " : ")
