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
