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

s1 = Student("Rahul", 20, 85)

print(s1.name)            # public
print(s1.get_age())       # protected (via getter)
print(s1.get_marks())     # private (via getter)

s1.set_age(21)            # protected (via setter)
s1.set_marks(90)          # private (via setter)

print(s1.get_age())
print(s1.get_marks())

#-----------------------------

# Inheritance


