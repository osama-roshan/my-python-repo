# Multiple inheritance 

class flayer:
    def fly(self):
        print("flying...")

class swimmer:
    def swim(self):
        print("swimming...")

class duck(flayer,swimmer):
    def quack(self):
        print("quack...")


d =  duck()
d.fly()
d.swim()
d.quack()


# Output

'''


flying...
swimming...
quack...

'''