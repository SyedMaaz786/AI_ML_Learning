# Python Operators 

# 1. Arithmetic Operators
a = 10
b = 3

print(a + b)                           
print(a - b)    
print(a * b)   
print(a / b)    
print(a // b)   
print(a % b)    
print(a ** b)   


# 2. Comparison Operators (returns True/False)
x = 5
y = 8

print(x == y)   
print(x != y)  
print(x > y)    
print(x < y)    
print(x >= y)   
print(x <= y)  


# 3. Logical Operators
p = True
q = False

print(p and q)  # AND → False
print(p or q)   # OR  → True
print(not p)    # NOT → False


# 4. Assignment Operators
num = 10
num += 5     # Same as num = num + 5
print(num)   # 15

num -= 3     # Same as num = num - 3
print(num)   # 12

num *= 2     # Same as num = num * 2
print(num)   # 24

num /= 4     # Same as num = num / 4
print(num)   # 6.0


# 5. Bitwise Operators (works on binary numbers)
a = 5      # 0101
b = 3      # 0011

print(a & b)   # AND  → 1 (0001)
print(a | b)   # OR   → 7 (0111)
print(a ^ b)   # XOR  → 6 (0110)
print(~a)      # NOT  → -6
print(a << 1)  # Left shift → 10
print(a >> 1)  # Right shift → 2


# 6. Identity Operators
m = [1, 2, 3]
n = m
o = [1, 2, 3]

print(m is n)      # True (same memory reference)
print(m is o)      # False (same value, different memory)
print(m is not o)  # True


# 7. Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True
print("orange" not in fruits) # True
