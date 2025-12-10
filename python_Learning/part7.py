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

