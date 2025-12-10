# Classes and objects in Python

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



