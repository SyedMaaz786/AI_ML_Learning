# Functions

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
