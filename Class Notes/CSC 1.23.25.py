# CSC 2053-002
# 1/23/25
# !!!!!!!!!!! EXAM ON THURSDAY (1/30) !!!!!!!!!!!
# *Today is thet last day of new content

# Inputs from the command line
name = input("Please enter your name: ")
print("Hello " + name)

num = input("Enter a number: ")
print("Your number is " + num)

double = num*2
print("Twice that is " + double)

# Note: because whatever number we enter is read as a STRING, performing math operations on it will not yield the desired results.
# Thus, we must instead typecast 'num' as a int
num = int(input("Try again: Enter a number: "))
print("Your new number is " + str(num))

double = num*2
print("New twice that is " + str(double)) 
# Print statements have a default '\n' at the end of the line. To remove this, you must have a " , end='' " after the statement in the print
# You may also use f-strings to embed variables/expressions into a print statement

'''
with  open("movies.txt") as file:
    for line in file:
        print(line)

with open("heights.text") as file:
    for line in file:
        info = line.strip().split()
        print(info)
        info[2] = int(info[2])
        print(info)
'''

# Prompt user to enter a file name, then print each lineof file with the line number
# C:\Users\borde\Downloads\CSC 2053-002 - Platform Based Computing\Class Notes\movies.txt
filename = input("Enter a filename/directory: ")
with open(filename) as file:
    count = 1
    for line in file:
        print(str(count) + ". " + line.strip())
        count += 1

# __init__ and __str__ are dunder methods. the double underscores mean that it is a special method/is a constructor, basically.
# Init basically is used to initialize the object, where we may then declare instance variables that we may assign values to


class BankAccount:
    def __init(self, account_number, bal = 0.0):
        self.account_number = account_number
        self.deposit = bal

from bank_account import BankAccount:

account1 = BankAccount('1234', 1000)
print(account1)
account1.deposit(1000)
