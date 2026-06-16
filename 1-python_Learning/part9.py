# OOP-Encapsulation, Inheritance, Abstraction, Polymorphism

# Encapsulation

class Student:
    def __init__(self, name, age, marks):
        self.name = name          # public
        self._age = age           # protected single underscore
        self.__marks = marks      # private double underscore

    # ----- GETTERS -----
    def get_age(self):
        return self._age

    def get_marks(self):
        return self.__marks

    # ----- SETTERS -----
    def set_age(self, new_age):
        self._age = new_age

    def set_marks(self, new_marks):
        self.__marks = new_marks

s1 = Student("Maaz", 20, 85)

print(s1.name)            # public
print(s1.get_age())       # protected (via getter)
print(s1.get_marks())     # private (via getter)

s1.set_age(21)            # protected (via setter)
s1.set_marks(90)          # private (via setter)

print(s1.get_age())
print(s1.get_marks())

#-----------------------------

# Inheritance

# ---------- 1. SINGLE INHERITANCE ----------
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):      # Single inheritance
    def bark(self):
        print("Dog barks")


# ---------- 2. MULTILEVEL INHERITANCE ----------
class BabyDog(Dog):      # Multilevel inheritance (Animal -> Dog -> BabyDog)
    def small_bark(self):
        print("Baby dog barks softly")


# ---------- 3. HIERARCHICAL INHERITANCE ----------
class Cat(Animal):       # Cat and Dog both inherit from Animal
    def meow(self):
        print("Cat meows")

class Cow(Animal):       # Another child of Animal
    def moo(self):
        print("Cow moos")


# ---------- 4. MULTIPLE INHERITANCE ----------
class Flyer:
    def fly(self):
        print("Can fly high")

class Bird(Animal, Flyer):   # Multiple inheritance (Animal + Flyer)
    def nature(self):
        print("Bird is an animal that can fly")

print("Single Inheritance:")
d = Dog()
d.sound()
d.bark()

print("\nMultilevel Inheritance:")
bd = BabyDog()
bd.sound()
bd.bark()
bd.small_bark()

print("\nHierarchical Inheritance:")
c = Cat()
c.sound()
c.meow()

cw = Cow()
cw.sound()
cw.moo()

print("\nMultiple Inheritance:")
b = Bird()
b.sound()
b.fly()
b.nature()

#-----------------------------

# Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod  # Here we are simply pass, and implement the details in the child class where, ie what is abstraction
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roars")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

l = Lion()
l.make_sound()

c = Cow()
c.make_sound()
#-----------------------------

# Polymorphism

# 1. METHOD OVERRIDING (Inheritance)
class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):   # overriding
        print("designation = Teacher")

# 2. METHOD OVERLOADING (Python way)
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# 3. OPERATOR OVERLOADING
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):     # using + operator
        return Number(self.value + other.value)

    def show(self):
        print("Value =", self.value)

# 4. DUCK TYPING (2 classes same fnx)
class Dog:
    def make_sound(self):
        print("Dog barks")

class Cat:
    def make_sound(self):
        print("Cat meows")



print("Method Overriding:")
t = Teacher()
t.get_designation()

print("Method Overloading:")
calc = Calculator()
print(calc.add(10))          
print(calc.add(10, 20))      
print(calc.add(10, 20, 30))

print("\nOperator Overloading:")
n1 = Number(30)
n2 = Number(20)
n3 = n1 + n2     # uses __add__
n3.show()

d = Dog() 
d.make_sound()

c = Cat()
c.make_sound()


