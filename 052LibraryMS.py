class Library:
    def __init__(self):
        self._no_of_books = 0
        self._books = []

    def print_books(self):
        for i in range(self._no_of_books):
            print(f'Book {i+1} : {self._books[i]}')
    
    def print_no_of_books(self):
        print(f'The Total Number of Books is : {self._no_of_books}')

a = Library()
first = True
while True:
    if first == True:
        print('Welcome to the Library !'.center(50))
        first = False
    print('\nWhat do you want?\n Enter 1 to add a book . \n Enter 2 to see all books. \n Enter 3 to see the number of books . \n Enter 4 to Quit .'.center(50))

    choice = int(input())
    if choice == 1:
        book = input('Enter the name of the book : ')
        a._books.append(book)
        a._no_of_books += 1 
    elif choice == 2 :
        a.print_books()
    elif choice == 3 :
        a.print_no_of_books()
    elif choice == 4 :
        break
    else:
        print("Invalid Choice")

