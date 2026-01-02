# Exception Handling 

try:
    num = int(input("Enter a number: ")) 
    result = 10 / num                      

except ValueError:
    print("You must enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Division successful:", result)   

finally:
    print("Program finished.")  

#------------------------------------------------------------------

# Comprehensions - The process of creating a new sequence from an existing one in a single line of code.

# List Comprehension

nums = [i for i in range(5)]
print(nums)

#----------------------------------------------------------------

squares = [i*i for i in range(5)]
print(squares)

#----------------------------------------------------------------

words = ["hello", "maaz", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)

#----------------------------------------------------------------

evens = [i for i in range(10) if i%2==0 ]
print(evens)

#----------------------------------------------------------------

nums = [3, -1, 5, -7, 2]
positive = [i for i in nums if i > 0]
print(positive)

#----------------------------------------------------------------

# Set Comprehension

s = {i for i in range(5)}
print(s)

#----------------------------------------------------------------

squares = {i * i for i in range(6)}
print(squares)

#----------------------------------------------------------------

letters = {ch for ch in "maaz"}
print(letters)

#----------------------------------------------------------------

evens = {n for n in range(10) if n % 2 == 0}
print(evens)

#----------------------------------------------------------------

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = {n for n in nums}
print(unique_nums)

#----------------------------------------------------------------

# Dictionary Comprehension

d = {i: i*i for i in range(5)}
print(d)

#----------------------------------------------------------------

names = ["Maaz", "Irfan", "Rizwan"]
lengths = {name: len(name) for name in names}
print(lengths)

#----------------------------------------------------------------

nums = [1,2,3,4,5]
even_square = {i: i*i for i in nums if i%2==0}
print(even_square)

#----------------------------------------------------------------

word = "hello"
freq = {char: word.count(char) for char in word}
print(freq)

# Generator Comprehension - It is just like a list comprehension but, Uses parentheses ( ) instead of brackets [ ]

gen = (i for i in range(5))  # generate output in the form of generator object
print(gen)

#----------------------------------------------------------------

gen = (n for n in range(10) if n % 2 == 0) 
print(list(gen))                           # So we do type casting to convert it into list to see the output


