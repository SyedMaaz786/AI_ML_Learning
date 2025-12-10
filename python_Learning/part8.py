# OOP-Classes and objects in Python

class Student:
    pass   # empty class

s1 = Student() # creating object
print(s1)

#--------------------------------

class Car:
    brand = "Toyota"  #properties/attributes
    color = "Red"

c1 = Car()      #creating object
print(c1.brand)
print(c1.color)

#--------------------------------

class Person:
    def greet(self):                   #self is the reference variable used to refer to the current object
        print("Hello, I am a person!")

p = Person()
p.greet()

#--------------------------------

class Animal:
    def __init__(self):         #Constructor(default)
        print("An Animal is created!")

#--------------------------------

class Student:
    def __init__(self, name , age):  #Constructor (init)
        self.name = name
        self.age = age

s1 = Student("Maaz", 22)
print(s1.name, s1.age)

#--------------------------------

class Dog:
    def __init__(self, name):         #Constructor(parameterized)
        self.name = name

    def bark(self):                    #Method
        print(self.name, "is barking!")

d1 = Dog("Tommy")
d1.bark()

#--------------------------------

class Mobile:
    def __init__(self, brand, price):  #Multiple objects with different properties
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 20000)
m2 = Mobile("Apple", 90000)

print(m1.brand, m1.price)
print(m2.brand, m2.price)

#--------------------------------

class Student:
    col_name = "ABC College"   #class property

    def __init__(self, name , age):
        self.name = name           #instance property
        self.age = age

s1 = Student("Syed", 23)
print(s1.name)

#--------------------------------

class Student:
    school_name = "ABC School"

    # INSTANCE METHOD
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # CLASS METHOD
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # STATIC METHOD
    @staticmethod
    def welcome_message():
        print("Welcome to the Student Portal!")

# Creating object (instance)
s1 = Student("Maaz", 22)

# Calling instance method
s1.show_details()

# Calling class method
Student.change_school("XYZ School")
print("Updated School Name:", Student.school_name)

# Calling static method
Student.welcome_message()

#--------------------------------


