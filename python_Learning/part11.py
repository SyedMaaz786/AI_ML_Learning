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
