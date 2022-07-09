"""Bill for borrowing the book"""
import datetime

def bill(billDetails,name):#need two parameters

    """store the year month date and microsecond. """
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    microsecond = datetime.datetime.now().microsecond
    """declaration of variables"""
    billDetailsIndex = 0
    borrowerName = ""
    totalCost = 0
    borrowedBooks = ""
    
    """Open file to write
        set the file name to the borrowers name
        add microsecond for uniqueness of the file to file name
    """
    file = open(name + "( " + str(microsecond) + " )","w")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                         Bill for borrowing the book")

    #loop to go through the list billDetails
    for i in range(0,len(billDetails)):
        #to access the data of the lists in billDetails 
        billDetailsIndex = billDetails[i]

        #for loop for storing the data in the list inside variables
        for j in range(0,len(billDetailsIndex)):
            if j == 0:
                borrowedBooks = borrowedBooks + "," + billDetailsIndex[j]
                
            if j == 1:
                borrowerName = billDetailsIndex[j]
                
            if j == 2:
                totalCost = totalCost + float(billDetailsIndex[j])
        #print the values of the stored variables
        if i == len(billDetails) - 1:
            print("Borrower name:" ,borrowerName)
            file.write("Borrower name:" + str(borrowerName) + "\n")
            print("Books Borrowed:" + borrowedBooks)
            file.write("Books borrowed:" + borrowedBooks + "\n")
            print("The total cost is: $",totalCost)
            file.write("The total cost is:" +"$"+ str(totalCost) + "\n")
            
    file.close()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

"""borrow books"""

def borrowBooks(bookIndex,nameOfBorrower):
    #open the file to write
    file = open("Books.txt","w")
    #declaration of variables and lists
    bookDetails = []
    totalBooksLeft = 0
    intitialAmountOfBooks = 0
    bookDetailslist = []
    bookList = []
    bookDetailIndex = 0
    billList = []
    billDetail = []
    bookName = ""
    costOfBook = 0.00
    checkBookID = False
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #ask the user for the bookID of the book to borrow
    while checkBookID == False:
        try:
            bookID = int(input("Enter ID of book you want to borrow:"))
            if bookID <= len(bookIndex) and bookID > 0:
                checkBookID = True
            else:
                print("Enter valid bookID that is available.")
        except:
            print("Please enter correct bookID.")
       
        

    #loop for borrowing the books
    for i in range(1,len(bookIndex) + 1):
        #to access the list in bookIndex list
        bookDetails = bookIndex[i-1]
        #to print the details of the book to be borrowed
        if i == bookID:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("                         Book Details")
            print("Book ID:",bookDetails[0])
            print("Author Name:",bookDetails[1])
            print("Book Name:",bookDetails[2])
            #to add all the books names to be borrowed and stored in bookName variable
            bookName = bookName + ", " + bookDetails[2]
            
            #to reduce the amount of books after borrowing
            intitialAmountOfBooks = int(bookDetails[3])
            totalBooksLeft = intitialAmountOfBooks - 1
            
            #print the amount of books left and that it has been decreased
            print("The amoubt of books has been decreased.")
            print("The amount of books left are:",totalBooksLeft)
            
            #change the amount of books available in the list booksDetails
            bookDetails[3] = totalBooksLeft
            
            print("The cost of books is:",bookDetails[4])

            #ask the user for the cost of the book
            costOfBook = float(input("Enter cost of the book: $"))

            #add the values of bookName, nameOfBorrower and costOfBook to the list billList
            billList.append(bookName)
            billList.append(nameOfBorrower)
            billList.append(costOfBook)
        #write the details of all the books to the file
        for j in range(1,6):
            file.write(str(bookDetails[j-1]))
            if j >= 1:
                file.write(",")
        file.write("\n")
        
    file.close()

    #retrun the list billList
    return billList
