# Basic Inheritance

class vehical:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} strating up ... ")

class car(vehical):

    def drive(self):
        print(f"{self.brand} is driving ...")


v = car("Toyota")
v.drive()
v.start ()

# Output

'''

Toyota is driving ...
Toyota strating up ... 

'''