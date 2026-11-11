# Class Vriables and intance variable 

class student:

    school = " Center of Excellence "

    def __init__(self, name:str ) -> None:
        self.name = name



s1 = student("Osama")
s2 = student("Saim")

print(s1.name) # instance variables
print(s2.name) # instance variables


print(s1.school) # class variables
print(s2.school) # class variables


# Output

'''

Osama
Saim
Center of Excellence 
Center of Excellence 

'''