# Multi-level inheritance 

class animal:
    def breath(self):
        print("brathing...")

class mamal(animal):
    def feed_young(self):
        print("feeding young...")
class dog(mamal):
    def bark(self):
        print("Woof")


d = dog()
d.breath()
d.feed_young()
d.bark()

# Output

'''

brathing...
feeding young...
Woof

'''
