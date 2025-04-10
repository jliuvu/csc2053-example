# 1/16/25

print(int(5/2)) # This will return a 2 when type casting 5/2, because it will chop off any decimal points, regardless of rounding

# While loop:
count = 0
while count < 5:
    print(count)
    count += 1

# For loop:
for i in range(1, 15, 2): # go from 1 thru 15, by increments of 2
    print(i, end = " ")

# Lists:
list = [2, 4, 6, 8]
print("\n")
for i in range(len(list)):
    print(i, list[i])

# The following is also prints all elements in a list:
for val in list:
    print(val, end = " ")

# This does the same thing as the code before the one above:
print("\n########################################\n")
for i, val in enumerate(list):
    print(i, val)

# EXERCISES:

# Ex. 1: Write a for loop to print all numbers from 1 to 20 that are divisible by 3
print("\n")
for i in range(1, 20):
    if (i%3 == 0):
        print(i, end = " ")

# Ex. 2: Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the result.
sum = 0
i = 1
print("\n")
while i < 51:
    if (i%2 == 0):
        sum += i
    i += 1
print(sum)

# Ex. 3: You are given a list of numbers: numbers = [5, 8, 2, 15, 10, 3, 7]. Use a for loop to print the numbers greater than 5.
print("\n")
numbers = [5, 8, 2, 15, 10, 3, 7]
for i in range(len(numbers)):
    if numbers[i] > 5:
        print(numbers[i], end = " ")

# Functions:
def hello_world():
    print("\nHello world!\n")

hello_world()

def hello(name):
    print("Hello " + name)
hello("heebees")
# You may also define a default input value:
def hello2(name = "odie"):
    print("Hello " + name)

hello2() # default 
hello2("Heebert") # input provided

# Functions exercise:

# Ex. 1:
def swap(input):
    print(input) # before
    length = len(input)
    temp = input[length - 1]
    input[length - 1] = input[0]
    input[0] = temp
    print(input) # swapped result

swap([1, 2, 3, 4, 5])

# String slicing:
course = "platform computing"
plat = course[0:8]
print(plat)
print(course[9:])