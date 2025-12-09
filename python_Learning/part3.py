# Type Casting (Explicit)

# 1. int() → convert to integer
num_str = "10"
num_int = int(num_str)
print(num_int, type(num_int))   # 10 <class 'int'>


# 2. float() → convert to float
num_str2 = "12.5"
num_float = float(num_str2)
print(num_float, type(num_float))  # 12.5 <class 'float'>


# 3. str() → convert to string
age = 22
age_str = str(age)
print(age_str, type(age_str))   # "22" <class 'str'>


# 4. bool() → convert to boolean
print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False (empty string)
print(bool("Maaz"))  # True (non-empty string)


# 5. list() → convert to list
my_tuple = (1, 2, 3)
print(list(my_tuple), type(list(my_tuple)))   # [1, 2, 3] <class 'list'>


# 6. tuple() → convert to tuple
my_list = [4, 5, 6]
print(tuple(my_list), type(tuple(my_list)))   # (4, 5, 6) <class 'tuple'>


# 7. set() → convert to set (removes duplicates)
my_list2 = [1, 2, 2, 3, 3, 3]
print(set(my_list2), type(set(my_list2)))     # {1, 2, 3} <class 'set'>


# Type Conversion (Implicit)
# Python converts types automatically

a = 10        # int
b = 3.5       # float

result = a + b   
print(result, type(result))  # 13.5 <class 'float'>


# Another implicit conversion example
x = 5
y = 2.0

print(x * y)        # 10.0 
print(type(x * y))  # <class 'float'>
