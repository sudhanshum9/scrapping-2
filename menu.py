from app import books

USER_CHOICE ="""Enter one of the following

-'b' to look at 5-star books
-'c' to look at the cheapest books
-'n' to just get the next book available book on the catalogue
-'q' to exit
enter your choice: """

def print_best_books():
    best_books= sorted(books,key=lambda  x: x.rating * -1)[:10]
    for book in best_books:
        print(book)

def print_chesapest_books():
    cheapest_books= sorted(books,key=lambda  x: x.price )[:10]
    for book in cheapest_books:
        print(book)

book_genrator=(x for x in books)
def print_next_book():
    print(next(book_genrator))

user_choices={
    'b': print_best_books,
    'c': print_chesapest_books,
    'n': print_next_book
}

def menu():
    choice = input(USER_CHOICE)
    while choice!='q':
        if choice in {'b','c','n'}:
            user_choices[choice]()
        else:
            print("Please choose a valid command.")
        choice=input(USER_CHOICE)

"""def menu():
    choice = input(USER_CHOICE)
    while choice!='q':
        if(choice=='b'):
            print("----best----")
            print_best_books()
        if(choice=='c'):
            print("----cheapest----")
            print_chesapest_books()
        if(choice=='n'):
            print("----next book----")
            print_next_book()
        if(choice=='q'):
            exit()
        choice = input(USER_CHOICE)
"""

menu()