# Functions

# PYTHON BUILT-IN FUNCTIONS 

# print()  → prints output on screen
# input()  → takes input from user
# type()   → returns the data type of a value
# len()    → returns length (string, list, tuple, etc.)
# int()    → converts value to integer
# float()  → converts value to float
# str()    → converts value to string
# bool()   → converts value to boolean
# range()  → generates a sequence of numbers
# sum()    → returns the sum of elements
# max()    → returns the largest value
# min()    → returns the smallest value
# abs()    → returns absolute value (positive)
# sorted() → sorts lists, tuples, etc.
# list()   → converts value into list
# tuple()  → converts value into tuple
# set()    → converts value into set
# dict()   → creates a dictionary
# round()  → rounds a number
# enumerate() → returns index + value in a loop
# zip()    → combines two or more sequences


# USER-DEFINED FUNCTIONS (CREATED BY THE USER)


def hello():
    print("Hello, World!")
hello()

# -------------------------------------------

def sum(a, b):
    return a + b

result = sum(3, 5)
print (result)

# -------------------------------------------

def calc_avg(a, b, c):
    return (a + b + c) / 3
average = calc_avg(4, 8, 12)
print(average)

# -------------------------------------------

def sum(a, b=1):
    return a + b
result = sum(5)
print(result)

# -------------------------------------------

# lambda FUNCTIONS - It is a small anonymous function, which does not require a def keyword.

add = lambda a, b: a + b     
print(add(2,3))