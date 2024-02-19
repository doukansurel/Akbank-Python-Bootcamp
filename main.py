import sys
import time

class Library:
    #------------------Constructor Methods---------------------
    def __init__(self):
        self.file= open("Books.txt","a+",encoding="utf-8")     
        self.control = True
        self.greeting()
    #------------------Destructor Methods--------------------
    def __del__(self):
        if self.file:
            self.file.close()
    #------------------Greeting Methods for Program---------------------
    def greeting(self):
        while(self.control):
            time.sleep(1.5)
            print("""
    ******* Welcome to Library Management System *******\n
                        1)List Books\n
                        2)Add Books\n
                        3)Remove Books\n
                        Q)Quit\n
                        H)Help\n
    ****************************************************              
                        """)
            print("""
Please make a choice:
                  """)
            self.choise = input("Your Choise:")
            if(self.choise.upper()=="Q"):
                self.control=False
                self.quitSystem()
            elif(self.choise.upper()=="H"):
                self.helpMethod()
                print("Please try again")
                time.sleep(1.5)
            elif(self.choise =="1"):
                self.listBooks()
            elif(self.choise =="2"):
                self.addBooks()
            elif(self.choise =="3"):
                self.removeBooks()
            else:
                print("Incorrect login, please try again or ask for help(H)")
    #Help method command => Success            
    def helpMethod(self):
        print("""
        Help:
        "1" => List Book: Lists the books registered in the library
        "2" => Add Book: Adds a book to the library record
        "3" => Remove Book: The book is deleted and updated from the library record.
        "Q" => System Exit
              """)
        time.sleep(4)
    #List Book => Success
    def listBooks(self):
        self.content = self.read_list()
        if not self.content:
            print("""
   ///////////////////////////////////////////////              
           No Books to List in the Library
   ///////////////////////////////////////////////  
                  """)
        else:
            for i in self.content:
                i = i.strip().split(",")
                book = f"Book:{i[0]} | Author:{i[1]}"
                print(book)        
    #Read book list is successful
    def read_list(self):
        self.content = []
        with open("Books.txt","r",encoding="utf-8") as f:
            self.content = f.read().splitlines()
        return self.content
    #Add a new book to the list of books => Success
    def addBooks(self):
        self.bookName_ = input("Enter book name:")
        self.authorName_ = input("Enter author name:")
        self.yearOfBook_ = input("Enter year of book:")
        self.pageNumber_ = input("Enter page number:")
        if self.bookName_=="" or self.authorName_=="" or self.yearOfBook_=="" or self.pageNumber_=="":
            print("Please check your entries")
            self.addBooks()
        else:
            new_Book = f"{self.bookName_},{self.authorName_},{self.yearOfBook_},{self.pageNumber_}"

            with open("Books.txt", "a",encoding="utf-8") as f:
                f.write(f"{new_Book}\n")
            print(f"{self.bookName_} book added successfully...")
    #remove books from the list of books => Success
    def removeBooks(self):
        delete_book = input("Enter the name of the book you want to delete:")
        if delete_book == "":
            print("Please check your entries")
            self.removeBooks()
        else:
            content = self.read_list()
            control = False
            file_="Books.txt"
            for i, line in enumerate(content):
                if line.startswith(delete_book):
                    delete_index = i
                    control = True
                    break
            if control==True:
                del content[delete_index]
                with open(file_, "w", encoding="utf-8") as f:
                    for line in content:
                        f.write(line + "\n")
                print(f"The book successfully deleted from the list.")    
            else:
                print("Book not found in the list. Please try again.")        
    #System quit => Success
    def quitSystem(self):
        print("""
        The system has been logged out...Have a good day!""")
        sys.exit()
   
if __name__ == "__main__":
    Library()
    


