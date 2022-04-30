class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendict = {}

    def displabook(self):
        print(f"This are the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lenbook(self, user, book):
        if book not in self.lendict.keys():
            self.lendict.update({book: user})
            print("Lender book database has been updated. You can take book now")
        else:
            print(f"Book is already being used by {self.lendict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book Has been Added to the Library")

    def retutnbook(self, book):
        self.lendict.pop(book)


if __name__ == '__main__':
    shivam = Library(["The Secret", "NO man's Land", "Ansi", "Python"], "Archives")
    print(f"Welcome to {shivam.name} Library")
    while (True):

        print("Enter your Choices")
        print("1.Display Book")
        print("2.len Book")
        print("3.Add Book")
        print("4.remove Book")
        user_choice = int(input())
        if user_choice == 1:
            shivam.displabook()
        elif user_choice == 2:
            book = input("Enter the Book you want: ")
            if book is not list:
                print("This book is not in our Archive ")
                continue
            name = input("Enter your name")

            shivam.lenbook(name, book)
        elif user_choice == 3:
            book = input("Enter the name of book you want to add to Library")

            shivam.addbook(book)
        elif user_choice == 4:
            book = input("Enter the name of book you want to return to Library")
            shivam.retutnbook(book)
        else:
            print("Not a valid Option")
        print("Press q to Quit and c to Continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue
            else:
                print("Not a valid Option")
