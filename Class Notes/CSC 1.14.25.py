# CSC 2053-002
# 1/14/25
# Topic: Introduction to Python

# Print statements:
print("Hello World!\n")
# this is a comment
x = 100
x = "hello"
x = [1, 2, 3]
print(x)

# Division operators:
x = 100
y = 10
print(x/y) # this results in a float output. To counter this, do x//y with two forward slashes (floor division)
print(x//y) # will chop off any floating point decimals
print(int(x/y)) # you can also just type cast it to an int

# Find minimum value:
min_val = min(1, 2, 3) # use LOWER CASE NAMING CONVENTION (no 'minVal', you must use all lower case with an _ if there is a space)
print(min_val) # returns the minimum value

# Raise number to power:
raised = pow(2, 3) # raises 2 to the power of 3
print(raised)
# you may use ** to represent the ^
new_raised = 2**3
print(new_raised)

# If statements:
x = -1
y = 0

if x < 0:
    print("X is negative")
    y += 1
elif x > 0:
    print("X is positive")
else:
    print("X is zero")

# for conditional and and or, use the words 'and' and 'or', rather than && and ||
start = 10
end = 100

if x > start and x < end:
    print("X is within range")
else:
    print("X is not in range")