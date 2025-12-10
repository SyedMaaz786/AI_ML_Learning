# String programs

s = "Hello Maaz"
print(s)

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
print(nums)

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
