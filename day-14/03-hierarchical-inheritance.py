# Hierarchical inheritance

class animal:
    def __init__(self,name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is brathing")

class dog(animal):
    def bark(self):
        print("Woof!")

class cat(animal):
    def mewo(self):
        print("Mewo")

class cow(animal):
    def gaa(self):
        print("gaaa")


d = dog("Rex")
c = cat("whiskers")
coow = cow ("bessi")

d.breathe()
c.breathe()
coow.breathe()

# Output

'''
Rex is brathing
whiskers is brathing
bessi is brathing

'''
