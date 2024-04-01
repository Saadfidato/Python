class Library:
    def __init__(self,booklist,ownername):
        self.booklist = booklist
        self.ownername = ownername
        self.lenDict = {}

    def displayBook(self):
        print(f"{self.ownername}, we have following books in our library.")
        sno = 1
        for book in self.booklist:
            print(f"{sno} {book}")
            sno+=1

    def lendBook(self,book,name):
        if book in self.booklist:
            if book not in self.lenDict:
                self.lenDict.update({book:name})
                print("Lender-Book database has been updated. You can take the book now.")
            else:
                print(f"Book is already being used by {self.lenDict[book]}")
        else:
            print(f"This book is not related to our database.")

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list.")

    def returnBook(self,book):
        if book in self.booklist:
            if book in self.lenDict.keys():
                self.lenDict.pop(book)
                print(f"Thank you. {book} book is received.")
            else:
                print(f"{book} book is not in use.")
        else:
            print(f"This book is not related to our database.")

if __name__ == '__main__':
    benlibrary = Library(['C','C++','Python','Java','ML'],'Ben')

    while(True):
        print(f"Welcome to the {benlibrary.ownername} library. Enter your choice to continue:")
        print("1 - Display Books")
        print("2 - Lend a Book")
        print("3 - Add a Book")
        print("4 - Return a Book")

        user_choice = int(input())
        
        if user_choice not in [1,2,3,4]:
            print("Please enter a valid option")
            continue
        else:
            if user_choice==1:
                benlibrary.displayBook()

            elif user_choice==2:
                book = input("Enter the name of the book you want to lend: ")
                user_name = input("Enter your name: ")
                benlibrary.lendBook(book,user_name)

            elif user_choice==3:
                book = input("Enter the name of the book you want to add: ")
                benlibrary.addBook(book)
                
            elif user_choice==4:
                book = input("Enter the name of the book you want to return: ")
                benlibrary.returnBook(book)

            else:
                print("Not a valid option.")

            print("Press Q to Quit or C to Continue")

            user_choice2 = ""

            while(user_choice2 != "C" and user_choice2 != "Q" ):
                user_choice2 = input()
                if user_choice2 == "Q":
                    exit()
                elif user_choice2 == "C":
                    continue    