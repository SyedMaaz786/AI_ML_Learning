# Conditional Statements Example (if, elif, else)

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent! Grade A")

elif marks >= 75:
    print("Good job! Grade B")

elif marks >= 50:
    print("You passed. Grade C")

else:
    print("Fail. Need improvement.")

# --------------------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("LOGIN successful")
elif username != "admin":
    print("Invalid username")
else: 
    print("Invalid password")


# --------------------------------------------------

n = int(input("Enter a number: "))

if n % 5 == 0 :
    print(f"{n} is divisible by 5")
else:
    print(f"{n} is not divisible by 5")


# --------------------------------------------------

n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is even")
else: 
    print(f"{n} is odd")


# --------------------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("LOGIN successful")
else:
    if username != "admin":
        print("Invalid username")
    else:
        print("Invalid password")