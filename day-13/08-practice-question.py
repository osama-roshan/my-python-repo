# Question 1

# students details using class and objects with using constructor


class student:
    def __init__(self, name:str, age: int, marks: list [int]) -> None:
        self.name =  name
        self.age = age
        self.marks = marks
    def total(self):
        return sum(self.marks)
    def avarage(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        avg = self.avarage()
        if avg >= 90:
            print("A")
        elif avg >= 50 and avg <=89:
            print("B")
        else:
            print("C")

student1 = student("Osama",19,[86,85,89,78,75])
total = student1.total()
print(total)
avg = student1.avarage()
print(avg)

student1.grade()

# Output

'''

413
82.6
B

'''

# Question 2

# Create a Student class with a class variable school and instance variables name and age. 
# Create two objects and print their details.


class Student:
    school = "UOL"

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Osama", 19)
s2 = Student("Ali", 20)

print(s1.name, s1.school)
print(s2.name, s2.school)

# Output

'''

Osama UOL
Ali UOL

'''

# Question 3

# Create a Bank class with a private balance. Use getter and setter methods to access and update the balance.

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

b1 = Bank(1000)

b1.set_balance(2000)
print(b1.get_balance())

# Output

'''

2000

'''

# Question 4

# Create a Parent class Animal with a method eat(). Create a child class Dog that inherits 
# Animal and has its own method bark().

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d1 = Dog()

d1.eat()
d1.bark()

# Outpur

'''

Animal is eating
Dog is barking

'''

# Question 5

# Create a parent class Vehicle with a method start(). Create a child class Car and override the start() method.


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

c1 = Car()
c1.start()

# Output

'''

Car is starting

'''