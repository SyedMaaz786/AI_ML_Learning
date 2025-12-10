# String programs

s = "Hello Maaz"
print(type(s))

#----------------------------------------------

name = "Maaz"

print(name[0])   
print(name[1])   
print(name[-1]) 

#----------------------------------------------

s = "Hello"

for ch in s:
    print(ch)

#----------------------------------------------

s = "Python"
print(len(s)) 

#----------------------------------------------

name = "Maaz"

print(name[0:2])   
print(name[1:4])   
print(name[:3])   
print(name[2:])    

#----------------------------------------------

s = "python"

print(s.upper())  
print(s.lower()) 

#----------------------------------------------

s = "hello world"

print("hello" in s)  
print("bye" in s)     

#----------------------------------------------

s = "banana"
print(s.count("a"))  

#----------------------------------------------

s = "I love Python"
new_s = s.replace("Python", "Coding")

print(new_s)   

#----------------------------------------------

text = "Python is fun"

words = text.split()   # ['Python', 'is', 'fun']
print(words)

joined = "-".join(words)
print(joined)          # Python-is-fun

#----------------------------------------------

s = "   hello   "

print(s.strip())  # hello
print(s.lstrip()) # left spaces removed
print(s.rstrip()) # right spaces removed

#----------------------------------------------

num = "12345"

print(num.isdigit())  # True

#----------------------------------------------

s = "hello"
print(s[::-1])   # olleh

#----------------------------------------------

#Lists programs

nums = [10, 20, 30, 40]
print(type(nums))

#----------------------------------------------

fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[-1])  # last item → mango

#----------------------------------------------

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'mango']

#----------------------------------------------

nums = [1, 2, 3]
nums.append(4)
print(nums)  # [1, 2, 3, 4]
nums.insert(1, 99)
print(nums)  # [1, 99, 2, 3, 4]

#----------------------------------------------

nums = [10, 20, 30, 40]

nums.remove(20)   # remove by value
print(nums)

nums.pop(1)       # remove by index
print(nums)

nums.pop()        # remove last element
print(nums)

#----------------------------------------------

fruits = ["apple", "banana", "mango"]

for x in fruits:
    print(x)

#----------------------------------------------

names = ["maaz", "ali", "zaid"]

if "maaz" in names:
    print("Found")

#----------------------------------------------

nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[2:])    # [30, 40, 50]

#----------------------------------------------

nums = [5, 2, 9, 1]

nums.sort()     # ascending
print(nums)

nums.reverse()  # reverse order
print(nums)

#----------------------------------------------

nums = [10, 20, 30]
print(len(nums))   # 3

#----------------------------------------------

details = ["Maaz", 22, 5.9, True]
print(details)

#----------------------------------------------

a = [1, 2, 3]
b = [4, 5]

a.extend(b)
print(a)  # [1, 2, 3, 4, 5]

#----------------------------------------------

nums = [10, 20, 30, 40, 50]  #Linear Search

x = 30
indx = 0

for val in nums:
    if val == x:
        print(f"Found at index {indx}")
        break
    indx += 1

#----------------------------------------------

# Tuple programs

t = (10, 20, 30, 40)
print(type(t))

#----------------------------------------------

t = ("apple", "banana", "mango")

print(t[0])   
print(t[2])  
print(t[-1])  

#----------------------------------------------

t = ("maaz", "ali", "zaid")

for name in t:
    print(name)

#----------------------------------------------

t = (10, 20, 30)
print(len(t))   

#----------------------------------------------

t = (10, 20, 30)

# t[1] = 50  # ❌ This will give error (tuple is immutable)

#----------------------------------------------

t = (10, 20, 30)

temp = list(t)     # convert to list
temp[1] = 99       # modify
t = tuple(temp)    # convert back to tuple

print(t)  # (10, 99, 30)

#----------------------------------------------

t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)

#----------------------------------------------

t = ("Maaz", 22, 5.9, True)
print(t)

#----------------------------------------------

t = (1, 2, (3, 4, 5))
print(t[2])      # (3, 4, 5)
print(t[2][1])   # 4

#----------------------------------------------

a = (1, 2, 3)
b = (4, 5)

c = a + b
print(c)   # (1, 2, 3, 4, 5)

#----------------------------------------------

t = (10, 20, 30, 20, 20)

print(t.count(20))   # 3
print(t.index(30))   # 2

#----------------------------------------------

# Set programs

s = {10, 20, 30, 40}
print(type(s))

#----------------------------------------------

s = {1, 2, 2, 3, 3, 3}
print(s)   # Output: {1, 2, 3}

#----------------------------------------------

s = {10, 20}

s.add(30)      # add one item
s.update([40, 50])  # add multiple items

print(s)

#----------------------------------------------

s = {10, 20, 30, 40}

s.remove(20)   # removes 20, gives error if not found
s.discard(50)  # no error even if 50 not found
s.pop()        # removes a random element

print(s)

#----------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a | b)            # same as union

#----------------------------------------------

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))   # {2, 3}
print(a & b)               # same

#----------------------------------------------

a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))   # {1}
print(b.difference(a))   # {4}

#----------------------------------------------

a = {1, 2, 3}
b = {2, 3, 4}

print(a.symmetric_difference(b))   # {1, 4}

#----------------------------------------------

# Dictionary programs

student = {
    "name": "Maaz",
    "age": 22,
    "course": "Python"
}

print(type(student))

#----------------------------------------------

student = {"name": "Maaz", "age": 22}

print(student["name"])   # Maaz
print(student["age"])    # 22

#----------------------------------------------

student = {"name": "Maaz"}

print(student.get("age"))        # None (no error)
print(student.get("age", "N/A")) # N/A

#----------------------------------------------

student = {"name": "Maaz", "age": 22} # Update value

student["age"] = 23
print(student)

#----------------------------------------------

student = {"name": "Maaz"} # Add new key-value pair

student["city"] = "Hyderabad"
print(student)

#----------------------------------------------

student = {"name": "Maaz", "age": 22, "city": "Hyderabad"}

student.pop("age")     # remove by key
student.popitem()      # removes last inserted item
del student["name"]    # delete key

print(student)

#----------------------------------------------

student = {"name": "Maaz", "age": 22}

for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, "=", value)

#----------------------------------------------

students = {
    "student1": {"name": "Maaz", "age": 22}, # Nested dictionary
    "student2": {"name": "Ali", "age": 20}
}

print(students["student1"]["name"])  # Maaz

#----------------------------------------------

student = {"name": "Maaz", "age": 22}

student.update({"age": 23, "city": "Hyderabad"})

print(student)

#----------------------------------------------



