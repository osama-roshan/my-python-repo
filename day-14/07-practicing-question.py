# Question 1
# Multilevel Inheritance
# Create three classes: Animal, Dog and Puppy. Use multilevel inheritance and call a method 
# from the first class.

class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def play(self):
        print("Playing...")

p = Puppy()
p.eat()
p.bark()
p.play()

# Output

'''
Eating...
Barking...
Playing...

'''

# Question 2

# Create two parent classes Father and Mother. Inherit both into a child class Child

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

# Output

'''
Driving
Cooking

'''

# Question 3

# Create one parent class Vehicle and two child classes Car and Bike. 
# Both should use the parent's method.

class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()

c.start()
b.start()

# Output

'''

Vehicle starting
Vehicle starting

'''

# Question 4

# Create a parent class Shape with an area() method. Override it in Rectangle and Circle

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2


shapes = [Rectangle(10, 5), Circle(5)]

for s in shapes:
    print(s.area())

# Output

'''

50
78.5

'''
# Questoion 5

# Create an abstract class Payment with an abstract method pay(). 
# Implement it in a child class and handle invalid payment using exception handling.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Cash(Payment):
    def pay(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Invalid amount")
            print("Payment successful:", amount)

        except ValueError as e:
            print(e)

p = Cash()
p.pay(500)
p.pay(-100)

# Output

'''

Payment successful: 500
Invalid amount

'''