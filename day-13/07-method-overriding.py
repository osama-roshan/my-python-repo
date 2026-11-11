# Method overriding

class animal:
    def speak(self):
        print("Animal is speaking")


class dog(animal):
    def speak(self):
        print(" dog is barking")


d = dog()
d.speak()

# Output

'''

dog is barking

'''