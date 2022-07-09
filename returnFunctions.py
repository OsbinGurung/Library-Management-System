import datetime
"""Bill for borrowing the book"""
def returnBill(borrowDate,name,booksReturned):#need two parameters

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
    allBooksReturned = ""
    dateList = []
    borrowYear = ""
    borrowMonth = ""
    borrowDay = ""
    fine = 0
    
    """Open file to write
        set the file name to the borrowers name
        add microsecond for uniqueness of the file to file name
    """
    file = open(name + "_" + str(microsecond) + "( Return Books )" ,"w")
    
    dateList.append(borrowDate.split("/"))
    for i in range(0,len(dateList)):
        dateListIndex = dateList[i]
        borrowYear = dateListIndex[0]
        borrowMonth = dateListIndex[1]
        borrowDay = dateListIndex[2]
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                         Bill for returning the book")
    for i in range(0,len(booksReturned)):
        allBooksReturned = allBooksReturned + "," + booksReturned[i]
        
    todayDate = str(year) + "/" + str(month) + "/" + str(day)
    print("Book borrow date:",borrowDate)
    print("Returned date:",todayDate)
    print("The books returned are :", allBooksReturned)
    if int(borrowYear) == year and int(borrowMonth) == month:
        #check days
        if day - int(borrowDay) <= 10 :
            print("No fine.")
        else:
            fine = (day - int(borrowDay)) * 0.5
            print("The fine is: $",fine)
    elif int(borrowYear) == year:
        #check months
        if int(borrowMonth) != month:
            if (day + 30) - int(borrowDay) <= 10 :
                print("No fine.")
            else:
                fine = ((day + 30) - int(borrowDay)) * 0.5
                print("The fine is: $",fine)

    file.write("Book borrow date:" + borrowDate + "\n")
    file.write("Today's date:" + todayDate + "\n")
    file.write("The books returned are :" + allBooksReturned + "\n")
            
    file.close()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

"""return books"""

def returnBooks(bookIndex):
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
    totalBooks = ""
    costOfBook = 0.00
    checkBookID = False
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #ask the user for the bookID of the book to return
    while checkBookID == False:
        try:
            bookID = int(input("Enter ID of book you want to return:"))
            if bookID <= len(bookIndex) and bookID > 0:
                checkBookID = True
            else:
                print("Enter valid bookID that is available.")
        except:
            print("Please enter correct bookID.")
        
    #loop for returning the books
    for i in range(1,len(bookIndex) + 1):
        #to access the list in bookIndex list
        bookDetails = bookIndex[i-1]
        #to print the details of the book to be returned
        if i == bookID:
            #to add all the books names to be returned and stored in totalBooks variable
            totalBooks = totalBooks + ", " +  bookDetails[2]
            
            #to increase the amount of books after borrowing
            intitialAmountOfBooks = int(bookDetails[3])
            totalBooksLeft = intitialAmountOfBooks + 1
            
            #print the amount of books left and that it has been increased
            print("Book Name:", bookDetails[2])
            print("The amoubt of books has been increased.")
            print("The amount of books left are:",totalBooksLeft)
            
            #change the amount of books available in the list booksDetails
            bookDetails[3] = totalBooksLeft

        #write the details of all the books to the file
        for j in range(1,6):
            file.write(str(bookDetails[j-1]))
            if j >= 1:
                file.write(",")
        file.write("\n")
    return(totalBooks)  
    file.close()


