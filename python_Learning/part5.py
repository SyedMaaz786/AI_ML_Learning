# FOR LOOP Examples

for i in range(1, 6):
    print(i)

# --------------------------------


for ch in "Maaz":
    print(ch)

# --------------------------------

for i in range(2, 11, 2):
    print(i)

# --------------------------------

for i in range(1 , 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd") 

# WHILE LOOP Examples

i = 1

while i <= 5:
    print(i)
    i += 1     


# --------------------------------

i = 5

while i >= 1:
    print(i)
    i -= 1


# --------------------------------

word = ""

while word != "stop":
    word = input("Type something (type 'stop') to end")


# --------------------------------

count = 1  #iteration variable
while (count <= 5):
    print("Hello, Maaz!", count)
    count += 1
print("After the loop, count =", count)

# --------------------------------

n = int(input("Enter a number to print its multiplication table: "))
i = 1
while(i <=10):
    print( n * i )
    i += 1

# --------------------------------

