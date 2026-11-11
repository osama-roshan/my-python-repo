# Setter and getter

class student:
    def __init__(self,name:str) -> None:
        self.__name = name

    # getter
    def get_name(self):
        return self.__name

    # setter

    def set_name(self, new_name: str):
        self.__name = new_name

s1 = student("Osama")
print(s1.get_name())
s1.set_name("XYZ")
print(s1.get_name())

# Output

'''

Osama
XYZ

'''