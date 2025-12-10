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