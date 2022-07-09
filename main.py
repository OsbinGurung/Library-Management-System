#import all function from borrow functions
from borrowFunctions import *
from returnFunctions import *
import datetime



""" to show the books available and the book details of the file"""
file = open("Books.txt","r")#open file
lines = file.readlines()#store the lines in the file

"""set list to empty"""
booksIndex = []
booksInfo = []
booksRow = []

"""add the values from the lines"""
for line in lines:
    """
        split the data from lines ',' as divider
        store the split data from a line in booksRow as a list
    """
    booksRow.append(line.split(","))
        
    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Book ID       Author Name       Book Name       Number of Books Available       Cost:")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#to print the data in the list bookRow
for k in range(len(booksRow)):
    #to access the lists inside booksRow list
    booksIndex = booksRow[k]
    print(booksIndex[0] + "            " + booksIndex[1] + "       " + booksIndex[2] + "            " + booksIndex[3] + "                 " + booksIndex[4] )
            
            
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

file.close()

def borrowReturn(inputNumber) :    
    file = open("Books.txt","r")
    lines = file.readlines()
    bookIndex = []
    billInfo = []
    billDetails = []
    counter = 0
    limitOfBooks = True
    year = ""
    month = ""
    day = ""
    borrowDate = ""
    totalBooks = ""
    returnedBooks = []
    dateCondition = True
    
    for line in lines:
        bookIndex.append(line.split(","))
        
    nameOfBorrower = input("Enter name of the borrower:")
    
    if inputNumber == 1:
        booksCounter = 0
        
        while limitOfBooks == True:
            
            try:
                numberOfBooks = int(input("How many books do you want to borrow?"))
                if(numberOfBooks <= 5):
                    limitOfBooks = False
                else:
                    print("Maximum number of books that can be borrowed is 5.")
            except:
                print("please enter a number.")
            
        
        while booksCounter < numberOfBooks:
            billInfo = borrowBooks(bookIndex,nameOfBorrower)
            billDetails.append(billInfo)
            booksCounter += 1
        bill(billDetails,nameOfBorrower)
        
    elif inputNumber == 2:
        
        todayYear = datetime.datetime.now().year
        todayMonth = datetime.datetime.now().month
        today = datetime.datetime.now().day
        while dateCondition == True:
            try:
                totalBooks = int(input("Enter the number of books to be returned:"))
                year = int(input("Enter the year the book was borrowed : "))
                month = int(input("Enter the month the book was borrowed : "))
                day = int(input("Enter the day the book was borrowed : "))
                if year > todayYear or month > todayMonth:
                    print("Please enter valid borrowed date of the books")
                    continue
                else:
                    dateCondition = False
            except:
                print("Please enter valid integer nnumbers.")
        
                
        borrowDate = str(year) + "/" + str(month) + "/" + str(day)
        
        while counter < totalBooks:
            returnedDetails = returnBooks(bookIndex)
            returnedBooks.append(returnedDetails)
            counter += 1
            
        returnBill(borrowDate,nameOfBorrower,returnedBooks)  
        #method call for return bill
    file.close()


"""While loop to not terminate progarm until user wants to """   
inputNumber = 0
while inputNumber != 3:
    print("Enter 1 to borrow books")
    print("Enter 2 to return a book")
    print("Enter 3 to exit")

    inputCondition = False
    """While loop for try and catch until user enters correct values."""
    while inputCondition == False:
        try:
            inputNumber = int(input("Enter a number:"))
            if inputNumber <=3 and inputNumber > 0:
                inputCondition = True
            else:
                print("Please enter a correct number.")
        except:
            print("Please enter a number.")
     
    if inputNumber == 1 or inputNumber == 2:
        #method call to borrow a book
        borrowReturn(inputNumber)
    elif inputNumber == 3:
        print("You have exited the program")
        
            


    
